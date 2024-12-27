# ASA to FMC Route Migrator

This Python script automates the migration of static routes from Cisco ASA to FMC-managed FTD devices. It's particularly useful when migrating from ASA to FTD and is designed to work with network objects that were previously migrated using the Firepower Migration Tool.

## Features

- Parses ASA static route configurations
- Matches existing network and host objects in FMC
- Supports objects created by Firepower Migration Tool ('obj-' prefix naming convention)
- Creates static routes in FMC for managed FTD devices
- Provides detailed progress and error reporting
- Includes safety checks and confirmation prompts