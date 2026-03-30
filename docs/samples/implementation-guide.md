# Implementation Guide — Carrier C (France)

!!! abstract "Sample type"
    **Carrier-specific implementation guide** — Covers accreditation requirements, station codes, fare rules, discount cards, and loyalty programs for a specific rail operator integration.

!!! note "Context"
    This sample documents the implementation specifics for a major French rail carrier. It guides integration partners through the unique requirements, station code conventions, fare combinations, and discount card handling needed to go live with this supply channel.

---

## Available API messages

The following API messages are **not available** for this carrier:

- addPaymentRequest w/Confirm¹
- authenticatePayerRequest
- deleteCardholderInfoRequest
- deletePaymentTokenRequest
- generatePaymentTokenRequest
- getIntermediateTravelPointsRequest

!!! info
    ¹ Available in certain circumstances when the platform operator is the merchant of record.

## Accreditation

The carrier's quality subsidiary ensures the quality of all products and services before their distribution to the public through sales and after-sales simulations on test environments. The quality team runs a comprehensive suite of tests against web applications to ensure all accreditation standards are met before a production launch.

For information about the accreditation requirements for each Supply Channel, please see the accreditation requirements summary.

## Station codes

A full list of station data codes for this carrier is available through the **Published Data API**, using the carrier identifier as the selection parameter.

**Example request**:
```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
  xmlns:pub="http://example.com/ws/publishing">
  <soapenv:Header/>
  <soapenv:Body>
    <pub:dataRequest type="station">
      <pub:parameters>
        <pub:selection>CARRIER_C</pub:selection>
      </pub:parameters>
    </pub:dataRequest>
  </soapenv:Body>
</soapenv:Envelope>
```

The station file structure for this carrier's stations is the same as all other suppliers.

**Example response**:
```xml
<pub:station code="AT@EB" countryCode="AT" fareStation="OUTPUT_ONLY"
  itineraryStation="YES" mainStation="NO" name="Ebensee"
  timeZone="Europe/Vienna" type="Group">
  <pub:supplier alias="81901929" codeType="UIC_UNI" source="CARRIER_C" type="CODE"/>
  <pub:supplier alias="ATEBE" codeType="CODE_RESARAIL" source="CARRIER_C" type="CODE"/>
  <pub:supplier alias="Ebensee" source="CARRIER_C" type="ALIAS"/>
  <pub:supplier source="CARRIER_C"/>
</pub:station>
```

## Special station codes

In addition to standard station codes, the implementation additionally supports station codes for two types of special stations:

- **Shared stations**
- **Group stations**

### Shared stations

A shared station is located on a route that crosses an international border and is serviced by two carriers. For example, London St. Pancras International is serviced by both this carrier and the UK carrier.

**Example**:
```xml
<pub:station code="GBQQS" countryCode="GB" fareStation="OUTPUT_ONLY"
  iataCode="QQS" itineraryStation="YES" latitude="51.532420"
  longitude="-0.126030" mainStation="NO"
  name="London St Pancras International" timeZone="Europe/London"
  type="Station">
  <pub:supplier alias="SPX" codeType="CRS" source="CARRIER_A" type="CODE"/>
  <pub:supplier alias="St Pancras International" source="CARRIER_A" type="ALIAS"/>
  <pub:supplier alias="70154005" codeType="UIC_UNI" source="CARRIER_C" type="CODE"/>
  <pub:supplier alias="GBSPX" codeType="CODE_RESARAIL" source="CARRIER_C" type="CODE"/>
  <pub:supplier alias="London St Pancras" source="CARRIER_C" type="ALIAS"/>
</pub:station>
```

The station code for a shared station is the same for both Suppliers, and the platform automatically determines which one to use when a shopping request is submitted.

### Group stations

A group station is a single station code that represents a collection of member stations within a geographical area, such as all the stations in a major city. Group station codes have a `type="Group"` attribute in the Published Data API to differentiate them from single-station codes `type="Station"`.

**Example**:
```xml
<pub:station code="FRABP" countryCode="FR" fareStation="OUTPUT_ONLY"
  itineraryStation="YES" mainStation="NO" name="Colomiers (localite)"
  timeZone="Europe/Paris" type="Group">
  <pub:supplier alias="3161146" codeType="UIC_UNI" source="CARRIER_C" type="CODE"/>
  <pub:supplier alias="Colomiers (localite)" source="CARRIER_C" type="ALIAS"/>
  <pub:supplier source="CARRIER_C"/>
</pub:station>
```

!!! info
    When a group station is specified as the origin or destination in the shopping request, the platform will return an individual member station in the response. For example, a journey to Paris might return the destination of Paris Gare du Nord.

## Combination fares

Certain fares for outbound/return can only be used in combination with each other.

In this case, the Point-to-Point Price for each leg in the shopping response includes a `<compatiblePrices>` element containing a list of `<compatiblePriceIDRef>` elements referencing the corresponding outbound or return prices with which the fare can be combined.

**Example**:
```xml
<compatiblePrices>
  <compatiblePriceIDRef>PRICE_1_1</compatiblePriceIDRef>
  <compatiblePriceIDRef>PRICE_1_2</compatiblePriceIDRef>
  <compatiblePriceIDRef>PRICE_1_3</compatiblePriceIDRef>
</compatiblePrices>
```

When the `createBookingRequest` message is submitted for a round trip, the platform verifies that the chosen Point-to-Point Prices are compatible with each other and **returns an error if not**.

!!! info
    Combination fare lists are included when a particular Ticketable Fare can only be combined with specific return Ticketable Fares. If there is no restriction based on the fares included in the Ticketable Fare, no combination fare list is provided.

## Loyalty cards

This carrier offers the ability to collect rewards through loyalty program(s). The first and last name on the order must match the name on the loyalty card for the loyalty card to be accepted.

A list of valid loyalty programs can be retrieved through the Published Data API.

**Example request**:
```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
  xmlns:pub="http://example.com/ws/publishing">
  <soapenv:Header/>
  <soapenv:Body>
    <pub:dataRequest type="loyaltyCard">
    </pub:dataRequest>
  </soapenv:Body>
</soapenv:Envelope>
```

**Example response**:
```xml
<pub:loyaltyCard description="Standard" marketingCarrier="CARRIER_C_EXPRESS"
  program="FR_STANDARD"/>
<pub:loyaltyCard description="Premium" marketingCarrier="CARRIER_C_EXPRESS"
  program="FR_PREMIUM"/>
<pub:loyaltyCard description="Premium Plus" marketingCarrier="CARRIER_C_INTERCITY"
  program="FR_PREMIUM_PLUS"/>
<pub:loyaltyCard description="Other card" marketingCarrier="CARRIER_C_INTERCITY"
  program="FR_OTHER"/>
```

The presence of a `<loyaltyCard>` element in the shopping response indicates that the loyalty program is available for a particular Leg Solution.

## Discount cards

Carrier C supports a number of discount cards that enable passengers to access reduced fares. Discount card data can be provided in the shopping request and is passed through to the carrier's inventory system to return eligible discounted fares.

The following discount cards are supported:

| Card | Description | Age restriction |
| :-- | :-- | :-- |
| Youth Card | 50% discount on eligible fares | 12–27 |
| Senior Card | 25% off peak, 50% off off-peak | 60+ |
| Weekend Card | 25% discount for weekend travel | None |
| Family Card | Group discount for 1–3 children travelling with an adult | Adult + children (4–11) |

**Example** — Including a discount card in the shopping request:
```xml
<com:passengerSpecification passengerTypeCode="A">
  <com:age>25</com:age>
  <com:discountCards>
    <com:discountCard>
      <com:discountCardProgram>FR_YOUTH_CARD</com:discountCardProgram>
      <com:discountCardNumber>1234567890</com:discountCardNumber>
    </com:discountCard>
  </com:discountCards>
</com:passengerSpecification>
```

## After-sales operations

### Exchanges

For this carrier, exchanges are supported where the fare conditions permit. The exchange workflow follows the standard API pattern:

1. Call `retrieveExchangeSummaryRequest` to get the available exchange options.
2. Call `searchForExchangeTicketsRequest` with the new journey details.
3. Call `processExchangeRequest` to complete the exchange.

### Cancellations

Cancellation rules vary by fare type. Some promotional fares are non-refundable. For refundable fares, cancellation fees may apply depending on how close to departure the cancellation is made.

!!! warning
    Always retrieve the cancellation summary first using `retrieveCancellationSummaryRequest` before processing the cancellation. The summary will show the applicable cancellation fee and the expected refund amount.
