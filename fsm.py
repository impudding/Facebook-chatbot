from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_image_url


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_state1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'romeo and juliet'
        return False

    def is_going_to_state2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'king lear'
        return False

    def is_going_to_state3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'othello'
        return False

    def is_going_to_state4(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'hamlet'
        return False
    
    def is_going_to_state5(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'a midsummer night\'s dream'
        return False
    
    def is_going_to_state6(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'the merchant of venice'
        return False
    
    def is_going_to_state7(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'much ado about nothing'
        return False
    
    def is_going_to_state8(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'twelfth night, or what you will'
        return False
    
    def is_going_to_stateR1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'juliet'
        
        return False

    def is_going_to_stateP1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'picture please'     
        return False

    def is_going_to_stateR2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'king lear'
        return False
    
    def is_going_to_stateP2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'picture please'     
        return False
    
    def is_going_to_stateR3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'lago'
        return False
    
    def is_going_to_stateP3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'picture please'     
        return False
    
    def is_going_to_stateR4(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'hamlet'
        return False

    def is_going_to_stateP4(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'picture please'     
        return False
    
    def is_going_to_stateR5(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'helena'
        return False
    
    def is_going_to_stateP5(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'picture please'     
        return False
    
    def is_going_to_stateR6(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'jessica'
        return False
    
    def is_going_to_stateP6(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'picture please'     
        return False

    def is_going_to_stateR7(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'claudio'
        return False
    
    def is_going_to_stateP7(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'picture please'     
        return False
    
    def is_going_to_stateR8(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'orsino'
        return False
    
    def is_going_to_stateP9(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'picture please'     
        return False
    
    def on_enter_state1(self, event):
        print("I'm entering state1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "Please answer who's speaking of this?\n O Romeo, Romeo! wherefore art thou Romeo?\
Deny thy father and refuse thy name;\n\
Or, if thou wilt not, be but sworn my love,\
And I\'ll no longer be a Capulet. ")
        #Juliet
        #self.go_back()

    def on_exit_state1(self, event):
        print('Leaving state1, go to next state')

        
        #Juliet
        #self.go_back()


    def on_enter_state2(self, event):
        print("I'm entering state2")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "Please answer who's speaking of this?\nNothing will come of nothing.")
        #King Lear
        #self.go_back()

    def on_exit_state2(self,event):
        print('Leaving state2')

    def on_enter_state3(self, event):
        print("I'm entering state3")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "Please answer who's speaking of this?\nTRIFLES LIGHT AS AIR ARE TO THE JEALOUS CONFIRMATIONS STRONG AS PROOFS OF HOLY WRIT.")
        #lago
        #self.go_back()

    def on_exit_state3(self,event):
        print('Leaving state3')
        
    def on_enter_state4(self, event):
        print("I'm entering state4")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "Please answer who's speaking of this?\nTo be, or not to be: that is the question:Whether \
’tis nobler in the mind to suffer The slings and arrows of outrageous fortune,\n\
Or to take arms against a sea of troubles,\
And by opposing end them?\nTo die: to sleep;\nNo more; and, by a sleep to say we end\
The heart-ache and the thousand natural shocks\
That flesh is heir to, ’tis a consummation \
Devoutly to be wish’d.\nTo die, to sleep;\
To sleep: perchance to dream: ay, there’s the rub.")
        #Hamlet
        #self.go_back()

    def on_exit_state4(self,event):
        print('Leaving state4')

    def on_enter_state5(self, event):
        print("I'm entering state5")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "Please answer who's speaking of this?\nLove looks not with the eyes, but with the mind,\
        And therefore is winged Cupid painted blind.")
        #self.go_back()

    def on_exit_state5(self,event):
        print('Leaving state5')

    def on_enter_state6(self, event):
        print("I'm entering state6")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "Please answer who's speaking of this?\nBut love is blind, and lovers cannot see\
        The pretty follies that themselves commit.")
        #jessica
        #self.go_back()

    def on_exit_state6(self,event):
        print('Leaving state6')

    def on_enter_state7(self, event):
        print("I'm entering state7")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "Please answer who's speaking of this?\nFriendship is constant in all other things,\
        Save in the office and affairs of love.")
        #Claudio
        #self.go_back()

    def on_exit_state7(self,event):
        print('Leaving state7')

    def on_enter_state8(self, event):
        print("I'm entering state8")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "Please answer who's speaking of this?\nIf music be the food of love, play on.")
        #Orsino
        #self.go_back()

    def on_exit_state8(self,event):
        print('Leaving state8')

    def on_enter_stateR1(self, event):
        print("I'm entering R1")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "good guess, you're right!")
        #juliet
        self.go_back()

    def on_exit_stateR1(self):
        print('Leaving R1')
    
    def on_enter_stateP1(self, event):
        print("I'm entering P1")

        sender_id = event['sender']['id']
        send_image_url(sender_id, "https://imgur.com/LfRg1U1.jpg")
        #juliet
        self.go_back()

    def on_exit_stateP1(self):
        print('Leaving P1')
    
    def on_enter_stateR2(self, event):
        print("I'm entering R2")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "good guess, you're right!")
        #juliet
        self.go_back()

    def on_exit_stateR2(self):
        print('Leaving R2')
    
    def on_enter_stateP2(self, event):
        print("I'm entering P2")

        sender_id = event['sender']['id']
        send_image_url(sender_id, "https://imgur.com/1GhMJLg.jpg")
        #juliet
        self.go_back()

    def on_exit_stateP2(self):
        print('Leaving P2')
    
    def on_enter_stateR3(self, event):
        print("I'm entering R3")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "good guess, you're right!")
      
        self.go_back()

    def on_exit_stateR3(self):
        print('Leaving R3')
    
    def on_enter_stateP3(self, event):
        print("I'm entering P3")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "https://imgur.com/oWkxakY.jpg")
      
        self.go_back()

    def on_exit_stateP3(self):
        print('Leaving P3')
    
    def on_enter_stateR4(self, event):
        print("I'm entering R4")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "good guess, you're right!")
        #juliet
        self.go_back()

    def on_exit_stateR4(self):
        print('Leaving R4')
    
    def on_enter_stateP4(self, event):
        print("I'm entering P4")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "https://imgur.com/nkanE6M.jpg")
        #juliet
        self.go_back()

    def on_exit_stateP4(self):
        print('Leaving P4')
    
    def on_enter_stateR5(self, event):
        print("I'm entering R5")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "good guess, you're right!")
        #juliet
        self.go_back()

    def on_exit_stateR5(self):
        print('Leaving R5')
    
    def on_enter_stateP5(self, event):
        print("I'm entering P5")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "https://imgur.com/kheB0yw.jpg")
        #juliet
        self.go_back()

    def on_exit_stateP5(self):
        print('Leaving P5')
    
    def on_enter_stateR6(self, event):
        print("I'm entering R6")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "good guess, you're right!")
        #juliet
        self.go_back()

    def on_exit_stateR6(self):
        print('Leaving R6')
    
    def on_enter_stateP6(self, event):
        print("I'm entering P6")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "https://imgur.com/Ft9nuS4.jpg")
        #juliet
        self.go_back()

    def on_exit_stateP6(self):
        print('Leaving P6')
    
    def on_enter_stateR7(self, event):
        print("I'm entering R7")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "good guess, you're right!")
        #juliet
        self.go_back()

    def on_exit_stateR7(self):
        print('Leaving R7')
    
    def on_enter_stateP7(self, event):
        print("I'm entering P7")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "https://imgur.com/8qtASIj.jpg")
        #juliet
        self.go_back()

    def on_exit_stateP7(self):
        print('Leaving P7')
    
    def on_enter_stateR8(self, event):
        print("I'm entering R8")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "good guess, you're right!")
        #juliet
        self.go_back()

    def on_exit_stateR8(self):
        print('Leaving R8')
    
    def on_enter_stateP8(self, event):
        print("I'm entering P8")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "https://imgur.com/gKI1Ff1.jpg")
        #juliet
        self.go_back()

    def on_exit_stateP8(self):
        print('Leaving P8')
    
    
    
    
    
    
    
    