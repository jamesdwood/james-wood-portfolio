# Platform Architecture: The SilverOne API

!!! abstract "Portfolio Context"
    **Role:** Lead Technical Writer  
    **Context:** This conceptual guide introduces our unified Open Sales and Distribution Model (OSDM) implementation. It explains to developers how multiple legacy railway integrators are aggregated behind a single asynchronous REST standard.
    **Key Skills:** Information architecture, distilling highly complex multi-tier architectural concepts into digestible explanations, applying industry standards (OSDM) to proprietary models.


:::(Error) (In this article, we will discuss the technical foundation, implementation patterns, and practical considerations for building applications with the SilverOne API. 

## Introduction
SilverOne is a standards-based retail platform that provides developers with a unified API for the complete rail and ground transport commerce journey. It is engineered to abstract away the complexity of a fragmented global mobility market, where integrating with multiple proprietary systems has traditionally been a major barrier to innovation.

Built on the [Open Sales & Distribution Model](https://osdm.io/){target="_blank"} (OSDM), SilverOne eliminates the need to connect to separate Mobility-as-a-Service (MaaS) aggregators or proprietary carrier links. Instead, it offers a single, consistent RESTful interface for the entire travel lifecycle: shopping, booking, fulfilment, and complex after-sales operations across global transport networks. This "common language" means a train journey and a bus leg are represented as predictable objects, dramatically simplifying the development of multi-modal itineraries.

Whether you are building a travel booking platform, integrating rail and bus inventory into an existing marketplace, or developing mobile applications for transport operators, SilverOne’s API is your strategic accelerator. It drastically reduces development time and maintenance overhead while providing access to an extensive and ever-expanding network of carriers worldwide.

## The advantages of SilverOne
Traditional rail and MaaS integrations require connecting to dozens of different APIs, each with unique data formats, authentication methods, and business rules. SilverOne solves this by providing:

•	*Single API integration* instead of multiple carrier/provider-specific implementations
•	*Standardized data models* based on the cross-industry OSDM specification
•	*Consistent authentication* using OAuth2 across all rail operators and MaaS providers
•	*Unified error handling* and response formats
•	*Real-time availability* and pricing from multiple sources

## API architecture and standards
SilverOne is built on OSDM, an open standard developed by industry leaders including DB, SBB, Amadeus, and SilverRail. OSDM defines:

•	*Standardized objects* for places, companies, service classes, passenger types, and facilities
•	*Common code* lists ensuring consistent data across different rail operators and MaaS providers
•	*Two operating modes*, **Retailer mode** for direct bookings and **Distributor mode** for third-party sales
•	*RESTful API design* with JSON request/response format
•	*OpenAPI 3.0 specification* for easy integration and code generation

The API supports the complete booking lifecycle from search to after-sales, with each endpoint designed for specific use cases while maintaining consistency across operations.

## Getting started
Ready to start building with SilverOne? Here’s how to get started:

1.	**Request API credentials** by raising a JIRA ticket
2.	**Explore the sandbox** environment with test data
3.	**Review our API reference** documentation for detailed endpoint specifications

## Authentication

To ensure secure communication, the SilverOne API uses the OAuth2 client credentials flow. This process allows your application to obtain a temporary access token that must be included in all subsequent API requests.

### Step 1 - Get API credentials
Before you can authenticate, you will need to raise a JIRA ticket to obtain a `client_id` and `client_secret`.

The `client_id` is a public, unique identifier for your application. The `client_secret` is a confidential key that must be stored securely on your server. Never expose this secret in client-side code.

### Step 2 - Request an access token
To get an access token, make a `POST` request to the test or production token endpoint. You must send your `client_id` and `client_secret` as `application/x-www-form-urlencoded parameters`.

**Test environment**:
```json
curl -X POST "https://test-api.silverrailtech.com/oauth2/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials" \
  -d "client_id=YOUR_CLIENT_ID" \
  -d "client_secret=YOUR_CLIENT_SECRET"
 ```
 
**Production environment**:
```json
curl -X POST "https://api.silverrailtech.com/oauth2/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials" \
  -d "client_id=YOUR_CLIENT_ID" \
  -d "client_secret=YOUR_CLIENT_SECRET"
```

### Step 3: Receive and Use the Access Token
A successful request returns a JSON object containing your access token and its expiration time (in seconds).

**Example response**:
```json
{
    "access_token": "eyJraWQiOiI2eFlWRnZ5SmdXNDJOTVwvUkxWZGVxNEZCbjJzb1RuSUhYTXRYS3VXV1FyST0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI1ODBrbXVuZTFjaHRrNnV4Znc1NmN3aWVuayIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiU2lsdmVyT25lQXBpXC9BY2Nlc3MiLCJhdXRoX3RpbWUiOjE3NTY5MTk3NDYsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5leGFtcGxlLmNvbVwvZXUtd2VzdC0xXzA1R29rb3c2IiwicmFuZG9tIjoiY2F0IiwiaWF0IjoxNzU2OTE5NzQ2LCJleHAiOjE3NTY5MjMzNDYsImp0aSI6IjZlOTUyZDI4LThmM2QtNDIxNC05YTY0LWFjNTFmNjIxODg5MSIsInZlcnNpb24iOjIsImNsaWVudF9pZCI6IjU4MGttdW5lMWNodGs2dXhmdzU2Y3dpZW5rIn0.E0j4n5pRnJ3aF9W7Ewj1mfZd6xNG1hN8cQ-Ucd_JiRDFtF1QZsS7b5vlN0YFJXe0kN-8hdbXWjJlS7c6RqujMNkd1JhG2qEmf0pJ6cSQXyMkX3T2JAXd3S_bJ3FJ2AqB-BaBNJu2oJwm9h2IrWj6k4Mu7s-HsHoazHo6vdTuSra_g7EzHBLVFMazeJyk0CiP0x40Kp5LcMYFsP9o6RM0LCn0nELDBPXE6hUv8umkkJrTYIuBsNBaG5C1k3xM1oagKPGcti4e9q0Ahdq34goa5GdWZ4p1UjLpNY0dcuGG4RtFhLra4p2mN8gRQUAhl4ir6ZqVmcU-50Dy4cBg",
    "expires_in": 3600,
    "token_type": "Bearer"
}
```

You must then include the `access_token` in the Authorization header of all subsequent API requests.

**Example /POST offers**:
```json
curl -X POST "https://test-api.silverrailtech.com/v1/offers" -H "Authorization: Bearer eyJraWQiOiI2eFlWRnZ5SmdXNDJOTVwvUkxWZGVxNEZCbjJzb1RuSUhYTXRYS3VXV1FyST0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI1ODBrbXVuZTFjaHRrNnV4Znc1NmN3aWVuayIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiU2lsdmVyT25lQXBpXC9BY2Nlc3MiLCJhdXRoX3RpbWUiOjE3NTY5MTk3NDYsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5leGFtcGxlLmNvbVwvZXUtd2VzdC0xXzA1R29rb3c2IiwicmFuZG9tIjoiY2F0IiwiaWF0IjoxNzU2OTE5NzQ2LCJleHAiOjE3NTY5MjMzNDYsImp0aSI6IjZlOTUyZDI4LThmM2QtNDIxNC05YTY0LWFjNTFmNjIxODg5MSIsInZlcnNpb24iOjIsImNsaWVudF9pZCI6IjU4MGttdW5lMWNodGs2dXhmdzU2Y3dpZW5rIn0.E0j4n5pRnJ3aF9W7Ewj1mfZd6xNG1hN8cQ-Ucd_JiRDFtF1QZsS7b5vlN0YFJXe0kN-8hdbXWjJlS7c6RqujMNkd1JhG2qEmf0pJ6cSQXyMkX3T2JAXd3S_bJ3FJ2AqB-BaBNJu2oJwm9h2IrWj6k4Mu7s-HsHoazHo6vdTuSra_g7EzHBLVFMazeJyk0CiP0x40Kp5LcMYFsP9o6RM0LCn0nELDBPXE6hUv8umkkJrTYIuBsNBaG5C1k3xM1oagKPGcti4e9q0Ahdq34goa5GdWZ4p1UjLpNY0dcuGG4RtFhLra4p2mN8gRQUAhl4ir6ZqVmcU-50Dy4cBg" -H "Content-Type: application/json" -d '{"tripSearchCriteria":{"origin":{"objectType":"GeoPositionRef","latitude":51.51419724575279,"longitude":-2.543114709917407},"destination":{"objectType":"GeoPositionRef","latitude":51.3781340962466,"longitude":-2.3559108891383023},"departureTime":"2025-09-23T10:00:00"},"anonymousPassengerSpecifications":[{"age":18,"externalRef":"PERSON_ONE","type":"PERSON"}]}'
```
 
#### A note on token expiration
Access tokens expire after the duration specified in the `expires_in` field (typically 1 hour). To improve performance, you should cache the access token on your server and reuse it until it expires. Once it expires, simply request a new one using the same process.

## Base URL
All API endpoints are available at:
`https://test-api.silverrailtech.com/` for our test environment
`https://api.silverrailtech.com/v1/` for our production environment.

## Basic workflow
1. **Search for available journeys** using [POST /offers](/v1-api/apidocs/returns-offers-for-trips-or-trip-search-criteria){target=`_blank`}
2. **Create a provisional booking** with [POST /bookings](/v1-api/apidocs/creates-a-booking-based-on-a-previously-requested-offer){target=`_blank`}
6.	**Partially update a provisional booking** with [PATCH /bookings](/v1-api/apidocs/updates-a-booking-but-does-not-confirm-the-booking){target="_blank"}. Supported update operations vary based on the carrier and market, and may include seat selections, payment details, and fulfilment methods.
7.	**Add passenger details and payment** information
8.	**Confirm the booking** to issue tickets
9.	Manage after-sales operations as needed

### Sample search request POST /v1/offers
```json
{
    "anonymousPassengerSpecifications": [
        {
            "externalRef": "PERSON_ONE",
            "type": "PERSON",
            "age": 44         }
    ],
    "tripSearchCriteria": {
        "origin": {
            "objectType": "GeoPositionRef",
            "latitude": 53.4765094,
            "longitude": -2.2383844         },
        "destination": {
            "objectType": "GeoPositionRef",
            "latitude": 51.5280408,
            "longitude": -0.135902         },
        "departureTime": "2025-09-01T18:40:00"     }
}
```

### Sample search response
```json
{
    "offers": [
        {
            "offerId": "94ac9822-60fd-411e-9e45-a4020d2d9a49",
            "summary": "V2|MAN|EUS|250901|1855|250901|2113|TRIP|MAN|EUS|250901|1855|250901|2113|VT7715|VT",
            "createdOn": "2025-09-01T15:56:11",
            "preBookableUntil": "2025-09-01T18:45:00",
            "passengerRefs": [
                "PERSON_ONE"             ],
            "products": [
                {
                    "id": "7f3c988c-d918-4e8c-8fb0-4dac8542daf2",
                    "summary": "Anytime Single",
                    "code": "SOS",
                    "owner": "urn:x_srt:rics:IWC",
                    "conditions": [...],
                    "flexibility": "SEMI_FLEXIBLE",
                    "isTrainBound": false,
                    "isReturnProduct": false,
                    "descriptiveTexts": [...]
                }
            ],
            "tripCoverage": {
                "coveredTripId": "1",
                "coveredLegIds": [
                    "2"                 ]
            },
            "admissionOfferParts": [...]
        }
    ],
    "anonymousPassengerSpecifications": [
        {
            "externalRef": "PERSON_ONE",
            "age": 44,
            "type": "PERSON"         }
    ],
    "trips": [
        {
            "id": "1",
            "duration": "PT2H31M",
            "direction": "OUT_BOUND",
            "startTime": "2025-09-01T18:45:00",
            "endTime": "2025-09-01T21:16:00",
            "legs": [
                {
                    "id": "1",
                    "transferLeg": {
                        "transferMode": "WALK",
                        "start": {
                            "objectType": "GeoPositionRef",
                            "latitude": 53.476509,
                            "longitude": -2.238384                         },
                        "end": {
                            "objectType": "StopPlaceRef",
                            "stopPlaceRef": "urn:uic:stn:700029680"                         },
                        "duration": "PT10M"                     }
                },
                {
                    "id": "2",
                    "timedLeg": {
                        "start": {
                            "stopPlaceRef": {
                                "stopPlaceRef": "urn:uic:stn:700029680"                             },
                            "stopPlaceName": "Manchester Piccadilly",
                            "serviceDeparture": {
                                "timetabledTime": "2025-09-01T18:55:00"                             },
                            "status": {...}
                        },
                        "end": {
                            "stopPlaceRef": {
                                "stopPlaceRef": "urn:uic:stn:700014440"                             },
                            "stopPlaceName": "London Euston",
                            "serviceArrival": {
                                "timetabledTime": "2025-09-01T21:13:00"                             },
                            "status": {...}
                        },
                        "service": {
                            "operatingDayRef": "2025-09-01",
                            "journeyRef": "UKRail:W09366_001",
                            "mode": {
                                "ptMode": "TRAIN"                             },
                            "publishedServiceName": "VT771500",
                            "vehicleNumbers": [
                                "W09366"                             ],
                            "serviceStatus": {
                                "unplanned": false,
                                "deviation": false                             },
                            "carriers": [
                                {
                                    "ref": "urn:x_srt:rics:GB:VT",
                                    "name": "Avanti West Coast"                                 }
                            ],
                            "attributes": [
                                {
                                    "text": "London Euston",
                                    "code": "Headsign"                                 }
                            ]
                        },
                        "duration": "PT2H18M"                     }
                }
            ],
            "tripStatus": {
                "unplanned": false,
                "cancelled": false,
                "deviation": false,
                "delayed": false             },
            "isOvertaken": false         }
    ],
    "tripContext": {
        "situations": [],
        "places": [
            {
                "objectType": "StopPlace",
                "ref": {
                    "stopPlaceRef": "urn:uic:stn:700029680"                 },
                "name": "Manchester Piccadilly",
                "id": "urn:uic:stn:700029680",
                "geoPosition": {
                    "longitude": -2.23091,
                    "latitude": 53.477361                 }
            }
        ]
    }
}
```

## Key features for developers
### Retail applications
- **Design once, deploy everywhere** - Standardized objects and code enable feature development across carriers without market-specific redesigns
- **Faster market entry** - Single integration provides access to multiple rail operators, mobility providers, and markets
- **Enhanced merchandising** - Explicit offers with clear pricing, conditions, and optional ancillaries support real basket-building without re-quoting

### Rail operator integrations
- **Expanded distribution** - Reach new channels and markets through standardized interfaces
- Reduced integration costs: One API standard eliminates multiple proprietary integration projects
•	**Future-proof architecture** - Open standard evolution ensures long-term viability
Enterprise features
- **Operational efficiency** - Consistent after-sales rules reduce exception handling
- **Improved analytics**: Standardized dimensions enable like-for-like comparisons across markets
- **Accelerated innovation** - Shared vocabulary and data structures speed feature development

## Data normalization with MasterData
SilverOne’s MasterData service handles the complexity of different rail operator data formats behind the scenes.  Instead of learning each carrier’s unique codes and conventions, developers work with a single, standardized set:

•	**Standardized location and carrier codes** -  All station, stop, and carrier identifiers are normalized to industry standards, primarily using UIC (International Union of Railways) codes where available
•	**Consistent passenger types** - A "Child" or "Senior" is a consistent entity across all carriers, with the MasterData service handling the translation to operator-specific age ranges or discount card requirements
•	**Unified service classes and amenities** - First class, second class, Wi-Fi, and power outlets are represented by standardized OSDM codes, allowing for consistent filtering and display in your UI
•	**Normalized pricing and currency** - All financial data is handled in a uniform structure, simplifying currency conversion and price comparison
•	**Standardized error codes and messaging** - Ambiguous supplier errors are translated into clear, actionable OSDM-standard error messages, making your error handling logic robust and simple.

During API calls, the MasterData service automatically translates between OSDM standard formats and carrier-specific requirements, ensuring your application code remains simple and consistent regardless of which rail operators you’re integrating with.

## Security and reliability

### Authentication and authorization
•	OAuth2 with client credentials for secure API access
•	AWS API Gateway with configurable rate limiting and throttling
•	JWT tokens with configurable expiration
•	IP allowlisting available for high-security environments

### Infrastructure
•	AWS-hosted with 99.9% uptime SLA
•	Auto-scaling to handle traffic spikes
•	Multi-region deployment for global performance
•	Real-time monitoring and alerting

### Development support
•	Sandbox environment for testing without affecting live bookings
•	OpenAPI specification for automated SDK generation
•	Comprehensive error codes with clear documentation
•	Webhook support for real-time booking updates

## Rail network coverage
SilverOne provides access to major rail operators across multiple regions.

### Europe
•	UK - All major train operating companies via Rail Delivery Group
•	France - SNCF domestic and international services
•	Spain - Renfe and Iryo
•	Sweden - SJ and regional operators via Samtrafiken
•	International - Eurostar, Thalys, and cross-border services

### North America
•	USA - Amtrak nationwide network
•	Canada - VIA Rail national network

## Integration partners
Leading travel platforms already using SilverOne include Google, Virgin Trains, Omio, Egencia, and major corporate travel management companies across Europe and North America.