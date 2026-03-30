# Release Notes — Platform 2.314 (S-326)

!!! abstract "Sample type"
    **Release notes** — Schema change analysis with breaking/non-breaking classification, detailed feature descriptions, error code documentation, and XML code examples.

!!! note "Context"
    These are production release notes for a biweekly platform release. They analyse XSD schema changes, classify them for partner impact, document new features with code examples, and list all enhancements and fixes.

---

## Key dates

| Production Deployment Date | Internal Release |
| :-- | :-- |
| 22 April, 2026 | S-326 |

## Schema changes summary

The following changes have been made to the XSD schemas in this release. **All schema updates in this release are entirely backwards-compatible (non-breaking).** Partners do not need to update their generated client code or XSDs unless they plan to implement the specific new features outlined below.

### CommonTypes

- **[Additive / Non-breaking]** The enumeration value `VOID_EXCEPTION_ON_INVALID` was added to `CancellationReasonType`. Existing integrations are unaffected, though partners using strict XSD validation on responses should ensure they can handle this new value gracefully.

### Booking Services

- **[Additive / Non-breaking]** The enumeration value `VOID_INVALID_BOOKING` was added to the `VoidOverrideType` element. Existing void overrides will continue working exactly as before.
- **[Additive / Non-breaking]** The new `seasonCancellationDate` (`xs:date`) element was added to `CancelBookingRequestType` and `RetrieveCancellationSummaryRequestType` to facilitate custom refund calculation dates for Season Tickets. Because this is an optional element, omitting it safely preserves the standard behavior (using the current date).
- **[Additive / Non-breaking]** New API operations `claimExternalValueDocumentRequest` and `claimExternalValueDocumentResponse` (and their associated types) were added. This introduces a new feature and does not affect any existing workflows or models.

### Shopping Services

- No structural changes in this release.

### Published Data Services

- No structural changes in this release.

---

## Custom calculation date for Season Ticket refunds

In previous releases, when calculating a refund for a Season Ticket using `retrieveCancellationSummaryRequest` and `cancelBookingRequest`, the platform always determined the refund amount against the **current date**.

A new `refundDate` request parameter has been added to these requests, allowing authorized Partners to specify an explicit date in the past for the season refund calculation. This feature gives Partners the flexibility to handle support scenarios like **retrospective refunds** for customers who were unable to travel (e.g., due to illness).

Validations have been put in place for this new parameter:

| Validation | Error Code | Message |
| :-- | :-- | :-- |
| Custom refund date on a non-season ticket | `BK00191` | *Cancel in the past is only allowed for season pass orders.* |
| Refund date is in the future | `BK00192` | *Cancellation date must not be in the future.* |
| Refund date before the season fare start date | `BK00193` | *Cancellation date must not be before the season fare start date.* |
| Parameter omitted | — | Standard behavior: uses date of request. |

**Example — cancelBookingRequest with custom refund date**:
```xml
<ns2:cancelBookingRequest dateTime="2026-03-24T10:15:30.000" version="2.0"
  xmlns="http://example.com/ws/commontypes"
  xmlns:ns2="http://example.com/ws/booking">
  <context>
    <distributorCode>DEMO</distributorCode>
    <pointOfSaleCode>GB</pointOfSaleCode>
    <channelCode>WEB</channelCode>
  </context>
  <ns2:recordLocator>B-DEMO-NSL002SFF</ns2:recordLocator>
  <ns2:orderLocator>O-DEMO-NSL002SFF-EPV000001</ns2:orderLocator>
  <ns2:refundDate>2026-03-10</ns2:refundDate>
  <ns2:expectedCancellationFee currency="GBP">0.00</ns2:expectedCancellationFee>
  <ns2:responseSpec>
    <ns2:returnReservationDetails>true</ns2:returnReservationDetails>
  </ns2:responseSpec>
  <ns2:selectedCancellationOption>
    <refundTarget type="FORM_OF_PAYMENT"/>
  </ns2:selectedCancellationOption>
</ns2:cancelBookingRequest>
```

---

## Carrier C — Mismatch between passenger and cardholder

For Carrier C bookings, the platform now maps specific warnings and errors returned when there is a mismatch between the passenger profile data provided and the carrier's data on file for the cardholder.

When a discrepancy is detected (e.g., names or date of birth), the platform will return one of two errors:

| Error code | Message |
| :-- | :-- |
| `SC00169` | *Name and/or date of birth of the cardholder do not match with the provided details. Please resolve to complete the booking.* |
| `WRN00020` | *Name and/or date of birth of the cardholder do not match with the provided details.* |

If such errors are encountered, Partners are advised to contact the customer to update their profile via the carrier's website or through the appropriate support channel.

---

## Booking error when requesting sleeper supplements on a return fare

A bug was identified when booking a return journey with sleeper supplements in both directions. If the `createBooking` request contained separate `optionalPrices` for the outward leg and the inward leg, the platform would fail the booking and return a `BK00201 - Inventory not available` error.

This logic has been **fixed**. The platform now correctly processes the `optionalPriceIDRef` for each leg independently, ensuring the correct sleeper supplement tariff is applied exclusively to the valid leg and allowing the return sleeper booking to succeed.

---

## Enhancements

| Ticket | Summary |
| :--- | :--- |
| SC-27897 | Backported barcode background to green for standalone seat reservations |
| SC-27873 | Barcode background to be green for standalone seat reservations |
| SC-27808 | Lead passenger information now provided as Customer contact in RARS bookings |

## Fixes

| Ticket | Summary |
| :--- | :--- |
| SC-27918 | Gaps in transaction number sequence in financial settlement when paying solely by voucher |
| SC-27817 | Null Pointer Exception — RARS request incorrect when booking sleeper supplements on a return fare |
| SC-27807 | Booking was sometimes failing when requesting sleeper supplement in both directions on a return fare |
| SC-27782 | Ticket by Mail (P2P and Season) — missing transaction number when paying solely by voucher |
