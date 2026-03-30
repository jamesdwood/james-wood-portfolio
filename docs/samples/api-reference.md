# API Reference — validateBookingResponse elements

!!! abstract "Sample type"
    **API reference documentation** — Element-by-element SOAP/XML response breakdown with schema annotations, attribute tables, and code examples.

!!! note "Context"
    This sample documents the response elements for a booking validation API call. The API returns information about a booking's validity, including travel segments, pricing, ticketing options, and payment requirements.

---

The response message consists of the following XML elements:

***

> **ns2:validateBookingResponse**

A container element for the response.

***

> validateBookingResponse
**requestStatus**

Status and error messages for the request. See SOAP Response Structure for a description of the status elements common to all API responses.

***

> validateBookingResponse
**ns2:bookingInformation**

A container element for all the validation information associated with the booking.

***

> validateBookingResponse
bookingInformation
**ns2:orderInformationSet**

A container element for one or more orders.

***

> validateBookingResponse
bookingInformation
orderInformationSet
**ns2:orderInformation**

An individual order. Most bookings contain only one order but there are various reasons why the response might be divided into multiple orders, for example, the booking contains tickets from more than one Supply Channel.

***

> validateBookingResponse
bookingInformation
orderInformationSet
orderInformation
**ns2:passengers**

A container element for all the passengers on this order. The structure is the same as the `<passengers>` element returned in the shopping response.

This element is only returned if the `<returnPricingDetails>` flag is set to `true` in the request.

***

> validateBookingResponse
bookingInformation
orderInformationSet
orderInformation
**ns2:legSolutions**

A container element for all the Leg Solutions on this order.

This element is only returned if the `<returnPricingDetails>` flag is set to `true` in the request.

***

> validateBookingResponse
bookingInformation
orderInformationSet
orderInformation
legSolutions
**legSolution**

An individual Leg Solution identified. The `legSolution` element has the following attribute:

| Attribute | Description |
| :-- | :-- |
| `legSolutionID` | The Id for the Leg Solution. |

**Example**:
```xml
<legSolution legSolutionID="LS_1_0">
```

!!! warning
    Although the `legSolutionId` attributes are numbered sequentially (LS_1_0, LS_1_1, LS_1_2, etc.), the Leg Solutions are not necessarily returned in order within the XML response and there may also be gaps in the sequence where the platform has filtered out unwanted results.

***

> validateBookingResponse
bookingInformation
orderInformationSet
orderInformation
legSolutions
legSolution
**numberOfConnections**

The number of connections contained in each Leg Solution.

**Example**:
```xml
<numberOfConnections>1</numberOfConnections>
```

***

> validateBookingResponse
bookingInformation
orderInformationSet
orderInformation
legSolutions
legSolution
**ns2:travelSegments**

A container element for the Travel Segments on this order.

***

> validateBookingResponse
bookingInformation
orderInformationSet
orderInformation
legSolutions
legSolution
travelSegments
**travelSegment**

An individual Travel Segment defining all or part of the journey as offered by this Leg Solution.

| Attribute | Description |
| --- | --- |
| `sequence` | An integer value indicating the chronological order of this Travel Segment within the Leg Solution. |
| `travelSegmentId` | A unique Id that identifies the Travel Segment in the format `LS_leg_leg solution_TS_Travel Segment`. For example: `LS_1_1_TS_2`. |
| `type` | The general method of transportation used for this Travel Segment: `TRAIN`, `BUS`, `FERRY`, `TAXI`, `SUBWAY`, `TRAM`, `HOVERCRAFT`, `TRANSFER` — Indicates a non-timetabled/scheduled Travel Segment. The `<equipmentType>` element shows the actual segment type (bus, walking, etc). |
| `legGrouping` | Indicates whether this Travel Segment is part of the outbound journey (legGrouping=1) or the return journey (legGrouping=2). |

**Example**:
```xml
<travelSegment sequence="0" travelSegmentID="LS_1_1_TS_0" type="TRAIN" legGrouping="2">
```

***

> validateBookingResponse
bookingInformation
orderInformationSet
orderInformation
legSolutions
legSolution
travelSegments
travelSegment
**originTravelPoint**

The Origin Travel Point for this Travel Segment, using the same format as the request message.

**Example**:
```xml
<originTravelPoint type="STATION">GBXVH</originTravelPoint>
```

***

> validateBookingResponse
bookingInformation
orderInformationSet
orderInformation
legSolutions
legSolution
travelSegments
travelSegment
**destinationTravelPoint**

The Destination Travel Point for this Travel Segment, using the same format as the request message.

**Example**:
```xml
<destinationTravelPoint type="STATION">GBQQM</destinationTravelPoint>
```

***

> validateBookingResponse
bookingInformation
orderInformationSet
orderInformation
legSolutions
legSolution
travelSegments
travelSegment
**departureDateTime**

The date and time of departure for this Travel Segment in YYYY-MM-DDTHH:MM:SS format (local to the Origin Travel Point).

**Example**:
```xml
<departureDateTime>2026-03-23T10:20:00</departureDateTime>
```

***

> validateBookingResponse
bookingInformation
orderInformationSet
orderInformation
legSolutions
legSolution
travelSegments
travelSegment
**arrivalDateTime**

The date and time of arrival for this Travel Segment in YYYY-MM-DDTHH:MM:SS format (local to the Destination Travel Point).

**Example**:
```xml
<arrivalDateTime>2026-03-23T12:28:00</arrivalDateTime>
```

***

> validateBookingResponse
bookingInformation
orderInformationSet
orderInformation
legSolutions
legSolution
travelSegments
travelSegment
**designator**

The train number as defined by the Supplier.

**Example**:
```xml
<designator>VT7070</designator>
```

***

> validateBookingResponse
bookingInformation
orderInformationSet
orderInformation
legSolutions
legSolution
travelSegments
travelSegment
**marketingCarrier**

The name of the transportation Carrier marketing the service for this Travel Segment. Typically, this value is the same as the `<operatingCarrier>` element.

**Example**:
```xml
<marketingCarrier>Carrier A</marketingCarrier>
```

***

> validateBookingResponse
bookingInformation
orderInformationSet
orderInformation
legSolutions
legSolution
travelSegments
travelSegment
**operatingCarrier**

The name of transportation Carrier providing the equipment for this Travel Segment. Typically this value is the same as the `<marketingCarrier>` element.

**Example**:
```xml
<operatingCarrier>Carrier B</operatingCarrier>
```

***

> validateBookingResponse
bookingInformation
orderInformationSet
orderInformation
legSolutions
legSolution
travelSegments
travelSegment
**equipmentType**

Provides additional detail about the transportation method for this Travel Segment. The `<equipmentType>` element has the following attribute:

| Attribute | Description |
| --- | --- |
| `code` | A three-letter abbreviation for the equipment type. |

The value of the element is the full equipment type description (High-speed, Commuter, Inter-City, etc). See content codes for a complete list of valid equipment types.

**Example**:
```xml
<equipmentType code="HSP">High-Speed</equipmentType>
```

***

> validateBookingResponse
bookingInformation
orderInformationSet
orderInformation
legSolutions
legSolution
travelSegments
travelSegment
**carbonData**

If provided by the supply system, returns the Kilograms of CO₂ emitted for each rail Travel Segment in the Leg Solution.

The `carbonData` element has the following attribute:

| Attribute | Description |
| :-- | :-- |
| unit | The unit of measurement used to express the amount of CO₂ emitted. |

**Example**:
```xml
<carbonData unit="kgCO2">11.1</carbonData>
```

***

> validateBookingResponse
bookingInformation
orderInformationSet
orderInformation
legSolutions
legSolution
travelSegments
travelSegment
**duration**

The length of this Travel Segment in xsd:duration format (PnYnMnDTnHnMnS).

**Example**:
```xml
<duration>P0Y0M0DT2H8M0S</duration>
```

***

> validateBookingResponse
bookingInformation
orderInformationSet
orderInformation
legSolutions
legSolution
travelSegments
travelSegment
**crossBorderInfo**

Returns `true` if this Travel Segment involves crossing a border where passengers are required to provide travel documents. Otherwise returns `false`.

**Example**:
```xml
<crossBorderInfo>false</crossBorderInfo>
```

!!! info
    From platform version 2.8 onwards, `<crossBorderInfo>` is superseded by the `<passengerInformationRequired>` element.

***

> validateBookingResponse
bookingInformation
orderInformationSet
orderInformation
legSolutions
legSolution
travelSegments
travelSegment
**marketingServiceName**

A description of the train or other transportation method. The text is either passed through from the Supplier or generated by the platform in the format "[operating carrier] service from [origin] to [destination]."

**Example**:
```xml
<marketingServiceName>Carrier A service from London Euston to Manchester Piccadilly</marketingServiceName>
```

***

> validateBookingResponse
bookingInformation
orderInformationSet
orderInformation
legSolutions
legSolution
travelSegments
travelSegment
**scheduleConfirmed**

Returns `false` if the Carrier has indicated that the schedule is subject to change. Otherwise returns `true`.

**Example**:
```xml
<scheduleConfirmed>false</scheduleConfirmed>
```

***

> validateBookingResponse
bookingInformation
orderInformationSet
orderInformation
**ns2:prices**

A container element for the collection of Point-to-Point Prices in the order. The structure is the same as the `<prices>` element returned in the shopping response.

This element is only returned if the `<returnPricingDetails>` flag is set to `true` in the request.

***

> validateBookingResponse
bookingInformation
orderInformationSet
orderInformation
**ns2:ticketingOptions**

A container element for all the ticketing options available on this order. The structure is the same as the Booking Record `<ticketingOptions>` element.

***

> validateBookingResponse
bookingInformation
orderInformationSet
orderInformation
**ns2:confirmationInformationRequired**

Determines whether the traveler must provide an Id to retrieve the value document or prove identity at time of travel.

***

> validateBookingResponse
bookingInformation
**ns2:paymentRequirements**

A container element for booking payment information. The structure is the same as the Booking Record `<paymentRequirements>` element.

***

> validateBookingResponse
bookingInformation
**ns2:serviceFeeAllowed**

Returns `true` if the booking allows service fees. Otherwise returns `false`. Normally, the platform allows you to add service fees to the booking using the updateBookingRequest. However, there are certain situations where service fees aren't permitted, such as when the rail supplier is the merchant of record.

**Example**:
```xml
<ns2:serviceFeeAllowed>true</ns2:serviceFeeAllowed>
```

***

> validateBookingResponse
bookingInformation
**ns2:creditCardSurchargeFeeApplicable**

Returns `true` if credit card fees are applicable to this booking. Otherwise returns `false`. If fees are applicable, the `<creditCardSurchargeFees>` element under `<paymentRequirements>` will indicate the amount for each affected card type.

**Example**:
```xml
<ns2:creditCardSurchargeFeeApplicable>true</ns2:creditCardSurchargeFeeApplicable>
```

***

> validateBookingResponse
bookingInformation
**ns2:passengerInformationRequired**

If this particular fare requires you to provide different information about the passengers at the time of booking than what was specified in the shopping response, the platform will include the `<passengerInformationRequired>` element.

**Example**:
```xml
<ns2:passengerInformationRequired>
  <ns2:passengerInformation allPassengers="false" type="PASSENGER_NAME"/>
  <ns2:passengerInformation allPassengers="false" type="PASSENGER_TITLE"/>
</ns2:passengerInformationRequired>
```
