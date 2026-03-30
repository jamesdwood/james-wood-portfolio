# Developer Guide — Create a booking

!!! abstract "Sample type"
    **Developer guide / workflow tutorial** — End-to-end documentation guiding developers through a core API operation, including request parameters, response handling, and code examples.

!!! note "Context"
    This sample documents the booking creation workflow — the second required step in any API message flow. It explains the inputs, the re-shopping behaviour, and the response structure, providing a clear path from shopping results to a confirmed booking.

---

## Overview

Creating a booking is the second required step in any API message flow and involves sending a `createBookingRequest` message that repeats the key data for whichever fare you selected from the shopping response.

You'll also need to provide additional passenger details such as names and contact information, along with any necessary reservation information. A successful request places the tickets on hold and establishes a set period of time during which you must complete the payment step.

![Booking workflow diagram — shopping to booking to payment](https://placehold.co/600x200/eee/999?text=Booking+Workflow+Diagram){width="50%"}

## Request

In its simplest form, the `createBookingRequest` message takes the following inputs:

| Input Parameter | XML Element |
| :-- | :-- |
| Every message passed into the API must include a **context**. This element contains five mandatory identifiers, which define your access to the API and which platform features you're authorized to use. | `<context>` |
| Notes about the booking. *(Optional)* | `<agentInformation>` `<notes>` |
| The names and ages of all the passengers travelling, plus contact information for at least one passenger. | `<passengers>` |
| A valid Leg Solution copied from the shopping response message. | `<legSolution>` |
| Price information for the chosen Leg Solution copied from the shopping response, plus an optional reservation request if seat assignments are available. | `<prices>` |
| Destination and pricing information copied from the travel pass shopping response. *(For Travel Pass bookings only)* | `<travelPassQuery>` |
| Additional parameters controlling the booking request, such as whether to accept a different ticket price and whether to include the complete Booking Record in the response message. *(Optional)* | `<parameters>` `<responseSpec>` |

Except for the passenger data and seat reservation request, all the necessary information is contained in the shopping response message.

When you submit the `createBookingRequest` message, the platform performs a **re-shop** using the Leg Solution data to make sure the tickets are still available and the pricing hasn't changed.

## Response

The resulting `createBookingResponse` message shows the success/fail status for the booking, assigns a unique **Booking Record locator Id**, and indicates the **hold date/time** after which the booking will be cancelled if not paid and confirmed.

The response message can also optionally echo back a complete Booking Record containing:

- Passenger information
- Travel Segments
- Ticketable Fares
- Full payment status and financials

---

## Request elements

The request message consists of the following XML elements:

***

> **ns2:createBookingRequest**

A container element for the request. The `createBookingRequest` element has the following attributes:

| Attribute | Description |
| :-- | :-- |
| `version` | The schema version. |
| `dateTime` | The date and time of the request. |

**Example**:
```xml
<ns2:createBookingRequest version="2.0" dateTime="2026-03-01T12:00:00">
```

***

> createBookingRequest
**context**

A container element for the five identifiers that define your access to the API.

| Element | Description |
| :-- | :-- |
| `distributorCode` | Your assigned distributor code. |
| `pointOfSaleCode` | The country code for the point of sale. |
| `channelCode` | The sales channel (WEB, MOBILE, AGENT, etc). |

**Example**:
```xml
<context>
  <distributorCode>DEMO</distributorCode>
  <pointOfSaleCode>GB</pointOfSaleCode>
  <channelCode>WEB</channelCode>
</context>
```

***

> createBookingRequest
**ns2:passengers**

A container element for all the passengers included in the booking. You must provide at least the passenger name, age, and contact details for the lead passenger.

**Example**:
```xml
<ns2:passengers>
  <ns2:passenger passengerID="PAX_SPEC_0">
    <ns2:nameFirst>John</ns2:nameFirst>
    <ns2:nameLast>Smith</ns2:nameLast>
    <ns2:contactInformation>
      <ns2:contact>
        <ns2:contactType>BUSINESS</ns2:contactType>
        <ns2:contactMedium>PHONE</ns2:contactMedium>
        <ns2:contactInfo>+44123456789</ns2:contactInfo>
      </ns2:contact>
    </ns2:contactInformation>
  </ns2:passenger>
</ns2:passengers>
```

***

> createBookingRequest
**ns2:legSolution**

A valid Leg Solution copied from the shopping response. This element defines the journey itinerary — origin, destination, departure/arrival times, and travel segments.

!!! warning "Important"
    The `<legSolution>` element must be copied exactly as returned in the shopping response. If any values are modified, the re-shop will fail and the booking will not be created.

***

> createBookingRequest
**ns2:prices**

The price information for the chosen Leg Solution, also copied from the shopping response. This element includes fare details, ticket class, and any applicable discounts.

If seat reservations are available and required, include a `<reservationRequest>` element within the price data.

***

> createBookingRequest
**ns2:parameters**

Optional parameters that control the booking behaviour.

| Element | Description |
| :-- | :-- |
| `<acceptPriceChange>` | If set to `true`, the booking will proceed even if the price has changed since the shopping request. If `false` (default), the booking will fail if the price differs. |
| `<holdDurationMinutes>` | Overrides the default hold duration. Not supported by all Supply Channels. |

**Example**:
```xml
<ns2:parameters>
  <ns2:acceptPriceChange>false</ns2:acceptPriceChange>
</ns2:parameters>
```

***

> createBookingRequest
**ns2:responseSpec**

Controls what data is returned in the response message.

| Element | Description |
| :-- | :-- |
| `<returnReservationDetails>` | Set to `true` to return the full Booking Record in the response. |

**Example**:
```xml
<ns2:responseSpec>
  <ns2:returnReservationDetails>true</ns2:returnReservationDetails>
</ns2:responseSpec>
```

---

## Example: One-way booking

The following example shows a simple one-way booking request for a single adult passenger.

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
  xmlns:book="http://example.com/ws/booking"
  xmlns:com="http://example.com/ws/commontypes">
  <soapenv:Header/>
  <soapenv:Body>
    <book:createBookingRequest version="2.0">
      <com:context>
        <com:distributorCode>DEMO</com:distributorCode>
        <com:pointOfSaleCode>GB</com:pointOfSaleCode>
        <com:channelCode>WEB</com:channelCode>
      </com:context>
      <book:passengers>
        <book:passenger passengerID="PAX_SPEC_0">
          <book:nameFirst>John</book:nameFirst>
          <book:nameLast>Smith</book:nameLast>
          <book:dob>1985-06-15</book:dob>
          <book:contactInformation>
            <book:contact>
              <book:contactType>BUSINESS</book:contactType>
              <book:contactMedium>EMAIL</book:contactMedium>
              <book:contactInfo>john.smith@example.com</book:contactInfo>
            </book:contact>
          </book:contactInformation>
        </book:passenger>
      </book:passengers>
      <!-- legSolution and prices copied from shopping response -->
      <book:legSolution legSolutionID="LS_1_0">
        <!-- ... -->
      </book:legSolution>
      <book:prices>
        <!-- ... -->
      </book:prices>
      <book:responseSpec>
        <book:returnReservationDetails>true</book:returnReservationDetails>
      </book:responseSpec>
    </book:createBookingRequest>
  </soapenv:Body>
</soapenv:Envelope>
```
