# Scope
A social experiment facilitating self-governance

## Proposals
- Anon/Non-anon
- Parlimentary Procedure (or equivalent)
    + Anon/Non-anon voting
- Voting system
    + Weighted based off contributions
        * Transportation = based of usage of public transport
        * Education = based off interactions with school system
            - Number of children
            - Did they attend the school themselves as children, etc.
- Funding
    + Supporter tap
        * Control $ per second
        * Control taps availability
- Multiple approval points throughout the process of proposal integration

## Voting Weighted Average Factors Tracking
- Cities
    + Transportation
        * Track user transporatation usage
        * Number of rides on bus, train, etc.
- Hackathon
    + Meals
        * Proposals
        * Deterministic Factors
            - Number of meals eaten
    + Sponsors
        * Proposals
        * Deterministic Factors
    + Prizes
        * Proposals
        * Deterministic Factors
            - Winners
            - Attendance
            - Wins

## Forum
- Anon/Non-anon threads
- Interface for discussion
    + Threads like reddit w/ comments/replies

## Hackathon MVP
- A chatbot for easier user onboard
- Proposals displayed on responsive web app

### Chatbot
Tech Stack:
- Flask
- Twilio
- PIL (Python Image Library)
    + Ex: [Python QR Decoder](https://github.com/allenywang/Python-QR-Decoder/blob/master/QRMatrix.py)

#### Iterative Steps
1. Recieve texts
2. Respond to texts
3. Recieve images and save to directory
4. Recieve images and parse QR code from image then return URL

### API
Tech stack:
- JavaScript

