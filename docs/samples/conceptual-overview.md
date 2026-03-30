# Conceptual Overview — Accessing the platform

!!! abstract "Sample type"
    **Conceptual / overview documentation** — High-level introduction to the platform environment model, access procedures, and accreditation process.

!!! note "Context"
    This sample provides an overview of the platform's environment structure and access model. It orients new integration partners, explains the certification and production environments, and describes the path to go-live.

---

## Environments

The platform maintains three separate environments, with two concurrent versions available for production and testing purposes at all times.

| Environment | Purpose | Connections | Downtime | Notes |
| :-- | :-- | :-- | :-- | :-- |
| **Certification-Next** | Test environment running the next scheduled release candidate | Test inventory, simulated billing | **Scheduled**: Saturday 0100 UTC to Monday 0200 UTC. **Deployment day**: 17:00–21:00 UTC | Each deployment purges bookings from the system |
| **Production** | Current live production environment | Live inventory, live billing | **Deployment day**: 00:00–04:00 UTC | |
| **Certification-Current** | Test environment running the same code as Production | Test inventory, simulated billing | **Deployment day**: 17:00–21:00 UTC | Each deployment purges bookings from the system |

!!! info
    For more information about the current versions installed in each environment, please see the release schedule. For a list of endpoint URLs, please see the Developer Guide.

## Accessing Certification environments

To access the test environments (Certification-Next and Certification-Current), you'll need:

1. An **SSL security certificate** issued by the platform operator.
2. A matching **test context** defining your access credentials and permissions.

To request a certificate and context, please contact your Account Manager.

## Accessing the Production environment

Before being granted access to the Production environment, your application must be **accredited** by the platform operator and by each supply channel. The accreditation process involves testing all transactions to ensure the application correctly implements the API.

---

## Implementation process

### Implementation tests

The platform has developed a set of implementation tests in cooperation with the carriers to ensure that distribution partners comply with all relevant obligations. All ticketing applications must pass these tests before authorization for production use.

In the course of these tests, the platform will verify that your application can:

- **Shop for** and successfully **book** a set of specific journeys on each Supply Channel to which you plan to connect.
- Meet the relevant **UI compliance standards** (if applicable).

To perform the necessary tests, the platform team will require access to your application after your implementation is complete.

!!! info
    Testing is performed using a pre-release environment because Supply Channels do not allow testing on production systems.

!!! info
    When a Partner releases new functionality and/or integrates new Supply Channels, the implementation must be re-evaluated using the same tests.

### Functional requirements

For a summary of the functional requirements for each Supply Channel, please see the Accreditation Requirements Summary.

### Sample implementation tests

Detailed test descriptions are available for each supported carrier:

- Carrier A (US)
- Carrier B (UK)
- Carrier C (France)
- Carrier D (Spain)
- Carrier E (Sweden)
- Carrier F (Canada)
