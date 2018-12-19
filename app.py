from bottle import route, run, request, abort, static_file

from fsm import TocMachine


VERIFY_TOKEN = "puddingVerifyTok"
machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2',
        'state3',
        'state4',
        'state5',
        'state6',
        'state7',
        'state8',
        'stateR1',
        'stateR2',
        'stateR3',
        'stateR4',
        'stateR5',
        'stateR6',
        'stateR7',
        'stateR8',
        'stateP1',
        'stateP2',
        'stateP3',
        'stateP4',
        'stateP5',
        'stateP6',
        'stateP7',
        'stateP8'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state4',
            'conditions': 'is_going_to_state4'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state5',
            'conditions': 'is_going_to_state5'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state6',
            'conditions': 'is_going_to_state6'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state7',
            'conditions': 'is_going_to_state7'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state8',
            'conditions': 'is_going_to_state8'
        },
        {
            'trigger': 'advance',
            'source':  'state1',
            'dest': 'stateR1',
            'conditions': 'is_going_to_stateR1'
        },
        {
            'trigger': 'advance',
            'source':  'state1',
            'dest': 'stateP1',
            'conditions': 'is_going_to_stateP1'
        },
        {
            'trigger': 'advance',
            'source':  'state2',
            'dest': 'stateR2',
            'conditions': 'is_going_to_stateR2'
        },
        {
            'trigger': 'advance',
            'source':  'state2',
            'dest': 'stateP2',
            'conditions': 'is_going_to_stateP2'
        },
        {
            'trigger': 'advance',
            'source':  'state3',
            'dest': 'stateR3',
            'conditions': 'is_going_to_stateR3'
        },
        {
            'trigger': 'advance',
            'source':  'state3',
            'dest': 'stateP3',
            'conditions': 'is_going_to_stateP3'
        },
        {
            'trigger': 'advance',
            'source':  'state4',
            'dest': 'stateR4',
            'conditions': 'is_going_to_stateR4'
        },
        {
            'trigger': 'advance',
            'source':  'state4',
            'dest': 'stateP4',
            'conditions': 'is_going_to_stateP4'
        },
        {
            'trigger': 'advance',
            'source':  'state5',
            'dest': 'stateR5',
            'conditions': 'is_going_to_stateR5'
        },
        {
            'trigger': 'advance',
            'source':  'state5',
            'dest': 'stateP5',
            'conditions': 'is_going_to_stateP5'
        },
        {
            'trigger': 'advance',
            'source':  'state6',
            'dest': 'stateR6',
            'conditions': 'is_going_to_stateR6'
        },
        {
            'trigger': 'advance',
            'source':  'state6',
            'dest': 'stateP6',
            'conditions': 'is_going_to_stateP6'
        },
        {
            'trigger': 'advance',
            'source':  'state7',
            'dest': 'stateP7',
            'conditions': 'is_going_to_stateP7'
        },
        {
            'trigger': 'advance',
            'source':  'state7',
            'dest': 'stateR7',
            'conditions': 'is_going_to_stateR7'
        },
        {
            'trigger': 'advance',
            'source':  'state8',
            'dest': 'stateR8',
            'conditions': 'is_going_to_stateR8'
        },
        {
            'trigger': 'advance',
            'source':  'state8',
            'dest': 'stateP8',
            'conditions': 'is_going_to_stateP8'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state1',
                'state2',
                'state3',
                'state4',
                'state5',
                'state6',
                'state7',
                'state8',
                'stateR1',
                'stateR2',
                'stateR3',
                'stateR4',
                'stateR5',
                'stateR6',
                'stateR7',
                'stateR8',
                'stateP1',
                'stateP2',
                'stateP3',
                'stateP4',
                'stateP5',
                'stateP6',
                'stateP7',
                'stateP8'
            ],
            'dest': 'user'
        },

        


    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)

@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="localhost", port=5000, debug=True, reloader=True)
    
