# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['network express-route peering connection'] = """
    type: group
    short-summary: Manage express route circuit connection with network
"""

helps['network express-route peering connection list'] = """
    type: command
    short-summary: "Gets all global reach connections associated with a private peering in an express route circuit."
    examples:
      - name: List ExpressRouteCircuit Connection
        text: |-
               az network express-route peering connection list --circuit-name "ExpressRouteARMCircuitA" \
--peering-name "AzurePrivatePeering" --resource-group "rg1"
"""

helps['network express-route'] = """
    type: group
    short-summary: Manage express route circuit with network
"""

helps['network express-route list-route-table-summary'] = """
    type: command
    short-summary: "Gets the currently advertised routes table summary associated with the express route circuit in a \
resource group."
    examples:
      - name: List Route Table Summary
        text: |-
               az network express-route list-route-table-summary --circuit-name "circuitName" --device-path \
"devicePath" --peering-name "peeringName" --resource-group "rg1"
"""

helps['network express-route show-peering-stat'] = """
    type: command
    short-summary: "Gets all stats from an express route circuit in a resource group."
    examples:
      - name: Get ExpressRoute Circuit Peering Traffic Stats
        text: |-
               az network express-route show-peering-stat --circuit-name "circuitName" --peering-name "peeringName" \
--resource-group "rg1"
"""

helps['network express-route wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the network express-route is met.
    examples:
      - name: Pause executing next line of CLI script until the network express-route is successfully created.
"""
