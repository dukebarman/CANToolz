from libs.module import *


class mod_firewall(CANModule):
    name = "Filter CAN messages"
    help = """
    
    This module block CAN messages by ID.
    
    Init parameters:  None
    
    Module parameters: 
    
      white_list - list of ID that should be filtered
      black_list - list of ID that should not be filtered
      pipe -       integer, 1 or 2 - from which pipe to print, default 1
      
      Example: {'white_list':[133,111]}
    
    """

    id = 4
    _active = True
    version = 1.0

    # Effect (could be fuzz operation, sniff, filter or whatever)
    def do_effect(self, can_msg, args):
        if can_msg.CANData:
            if can_msg.CANFrame.frame_id in args.get('black_list', []):
                can_msg.CANData = False
                self.dprint(2, "Message " + str(can_msg.CANFrame.frame_id) + " has been blocked (BUS = " + str(
                    can_msg.bus) + ")")
            elif 'white_list' in args and can_msg.CANFrame.frame_id not in args.get('white_list',[]):
                can_msg.CANData = False
                self.dprint(2, "Message " + str(can_msg.CANFrame.frame_id) + " has been blocked (BUS = " + str(
                    can_msg.bus) + ")")
        return can_msg
