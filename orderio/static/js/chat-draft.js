

let loc = window.location
let wsStart = 'ws://'
const USER_ID = $('#logged-in-user').val()
if(loc.protocol === 'https') {
    wsStart = 'wss://'
}
let endpoint = wsStart + loc.host + loc.pathname
let input_message = $('#input-message')
let message_body = $('.msg_card_body')
let send_message_form = $('#send-message-form')
var socket = new WebSocket(endpoint)
$( document ).ready(function() {
    console.log( "ready!" );
    message_body.scrollTop(message_body.prop("scrollHeight"));
    
});


socket.onopen = async function(e){
    console.log('open', e)
    send_message_form.on('submit', function (e){
        e.preventDefault()
        let message = input_message.val()
        let send_to = get_active_other_user_id()
        let thread_id = get_active_thread_id()

        let data = {
            'message': message,
            'sent_by': USER_ID,
            'send_to': send_to,
            'thread_id': thread_id
        }
        data = JSON.stringify(data)
        socket.send(data)
        $(this)[0].reset()
    })
}

socket.onmessage = async function(e){
    console.log('message', e)
    let data = JSON.parse(e.data)
    let message = data['message']
    let sent_by_id = data['sent_by']
    let thread_id = data['thread_id']
    newMessage(message, sent_by_id, thread_id)
}

socket.onerror = async function(e){
    console.log('error', e)
}

socket.onclose = async function(e){
    console.log('close', e)
}


function newMessage(message, sent_by_id, thread_id) {
	if ($.trim(message) === '') {
		return false;
	}
	let message_element;
	let chat_id = 'chat_' + thread_id
    let date = new Date()
	if(sent_by_id == USER_ID){
	    message_element = `
        <div class="media w-50 ml-auto mb-3">
        <div class="media-body">
          <div class="bg-primary rounded py-2 px-3 mb-2">
            <p class="text-small mb-0 text-white">${message}</p>
          </div>
          <p class="small text-muted text-uppercase">${("0" + date.getHours()).slice(-2)}:${date.getMinutes()} | ${("0" + date.getDay()).slice(-2)}-${date.toLocaleString('default', { month: 'short' })}-${date.getFullYear()}</p>
        </div>
      </div>
	    `
    }
	else{
	    message_element = `
        <div class="media w-50 mb-3">
        <img src="https://bootstrapious.com/i/snippets/sn-chat/avatar.svg" alt="user" width="50" class="rounded-circle">
        <div class="media-body ml-3">
          <div class="bg-dark rounded py-2 px-3 mb-2">
            <p class="text-small mb-0 text-white">${message}</p>
          </div>
          <p class="small text-muted text-uppercase">${("0" + date.getHours()).slice(-2)}:${date.getMinutes()} | ${("0" + date.getDay()).slice(-2)}-${date.toLocaleString('default', { month: 'short' })}-${date.getFullYear()}</p>
        </div>
      </div>
        `

    }

    let message_body = $('#messages-wrapper[chat-id="' + chat_id + '"] .msg_card_body')
	message_body.append($(message_element))
    message_body.scrollTop(message_body.prop("scrollHeight"));
    
	input_message.val(null);
}
$('.list-group a').on('click', function (){
    $('.active').removeClass('active')
    $(this).addClass('active')

    // message wrappers
    let chat_id = $(this).attr('chat-id')
    $('#messages-wrapper.is_active').removeClass('is_active')
    $('#messages-wrapper[chat-id="' + chat_id +'"]').addClass('is_active')
    $("#msg_card_body"+chat_id).scrollTop($("#msg_card_body"+chat_id).prop("scrollHeight"));
})

function get_active_other_user_id(){
    let other_user_id = $('#messages-wrapper.is_active').attr('other-user-id')
    other_user_id = $.trim(other_user_id)
    return other_user_id
}

function get_active_thread_id(){
    let chat_id = $('#messages-wrapper.is_active').attr('chat-id')
    let thread_id = chat_id.replace('chat_', '')
    return thread_id
}



