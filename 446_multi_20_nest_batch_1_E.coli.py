from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'My Protocol',
    'author': 'Name <email@address.com>',
    'description': 'Simple protocol to get started using OT2',
    'apiLevel': '2.8'
}

# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions
def run(protocol: protocol_api.ProtocolContext):

    # labware
    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '3')
    tiprack = protocol.load_labware('opentrons_96_filtertiprack_200ul', '1')
    reservoir = protocol.load_labware('nest_12_reservoir_15ml', '2')
    
    # pipettes
    p300_multi = protocol.load_instrument('p300_multi_gen2', 'left', tip_racks=[tiprack])


    # commands
    # for i in range(3):
    #    p300_multi.distribute(100, reservoir.wells()[i], plate.columns()[i])

    # loop of 12
    for i in range(12):
       p300_multi.distribute(100, reservoir.wells()[i], plate.columns()[i])

    # loop of 8
    # for i in range(8):
    #    p20_multi.distribute(1, reservoir.wells()[i], plate.columns()[i])