# ASA to FMC Route Migrator

This Python script automates the migration of static routes from Cisco ASA to FMC-managed FTD devices. It's particularly useful when migrating from ASA to FTD and is designed to work with network objects that were previously migrated using the Firepower Migration Tool.

## Features

- Parses ASA static route configurations
- Matches existing network and host objects in FMC
- Supports objects created by Firepower Migration Tool ('obj-' prefix naming convention)
- Creates static routes in FMC for managed FTD devices
- Provides detailed progress and error reporting
- Includes safety checks and confirmation prompts

## Prerequisites

- Python 3.6 or higher
- `requests` library (`pip install requests`)
- Network and host objects should already exist in FMC (typically migrated using Firepower Migration Tool)
- FMC API access

## Installation

1. Clone this repository:
```bash
git clone https://github.com/MediocreTriumph/asa-to-fmc-route-migrator.git
cd asa-to-fmc-route-migrator
```

2. Install required packages:
```bash
pip install requests
```

## Usage

1. Update the configuration parameters in the script:
```python
FMC_HOST = "your_fmc_hostname"  # FMC hostname/IP
USERNAME = "your_username"      # FMC username
PASSWORD = "your_password"      # FMC password
DEVICE_NAME = "your_ftd_name"   # FTD device name in FMC
ROUTES_FILE = "asa-routes.txt"  # Path to your routes file
```

2. Run the script:
```bash
python asaToFMCrouteMigrator.py
```

The script will:
- Connect to FMC
- Find your FTD device
- Load existing network/host objects
- Parse your ASA routes
- Match routes with existing objects
- Ask for confirmation before deployment
- Deploy routes to FTD via FMC

## Object Naming Convention

The script expects network and host objects in FMC to follow the Firepower Migration Tool naming convention:
- Host objects: `obj-{ip_address}`
- Network objects: `obj-{network_address}`

Example:
- Host object for 192.168.1.1: `obj-192.168.1.1`
- Network object for 10.1.1.0/24: `obj-10.1.1.0`

## Error Handling

The script includes several safety features:
- Validates all required objects exist before attempting deployment
- Lists any missing objects that need to be created
- Stops deployment immediately if any route fails
- Provides detailed error messages and route details on failure

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details

## github_api_enhancement.py

This file was generated as a proof of concept when MCP errors were encountered during attempts by Claude to push the fmc_route_converter.py file to this repository. It is here in case it is useful to Anthropic for improving Claude's integration with GitHub.
