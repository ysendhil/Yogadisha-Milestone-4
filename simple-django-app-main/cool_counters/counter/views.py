from django.shortcuts import render, get_object_or_404
from .models import Counter
from django.shortcuts import redirect
from .forms import ItemForm
from .models import ItemInfo  # Update the import
from .forms import AddItemForm  # Import the new form
from django.contrib import messages  # Import messages to display flash messages



def home(request):
    return render(request, 'counter/home.html')


def list(request):
    items = ItemInfo.objects.all()
    return render(request, 'counter/list.html', {'items': items})


def item_detail(request, item_id):
    counter = get_object_or_404(ItemInfo, pk=item_id)
    return render(request, 'counter/item_detail.html', {'counter': counter})


def authenticate_user(username, password):
    # Hard-coded username and password for demonstration purposes
    demo_username = 'demo_user'
    demo_password = 'demo_password'

    return username == demo_username and password == demo_password


def add_item(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if authenticate_user(username, password):
            form = AddItemForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('list')
        else:
            messages.error(request, 'Authentication failed. Please check your username and password.')

    else:
        form = AddItemForm()

    return render(request, 'counter/add_item.html', {'form': form})


def edit_item(request, item_id):
    item = get_object_or_404(ItemInfo, pk=item_id)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if authenticate_user(username, password):
            form = ItemForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('list')
        else:
            messages.error(request, 'Authentication failed. Please check your username and password.')

    else:
        form = ItemForm(instance=item)

    return render(request, 'counter/edit_item.html', {'form': form})




def chatbot(request):
    if request.method == 'POST':
        user_message = request.POST.get('user_message')
        chatbot_response = respond_to_user(user_message)  # Replace with your chatbot logic

    else:
        user_message = ''
        chatbot_response = 'Hello! How can I assist you today?'

    return render(request, 'counter/chatbot.html', {
        'user_message': user_message,
        'chatbot_response': chatbot_response,
    })

def respond_to_user(user_message):
    # Replace this logic with your chatbot's response logic
    if 'hello' in user_message.lower():
        return 'Hello! How can I assist you today?'
    elif 'goodbye' in user_message.lower():
        return 'Goodbye! Have a great day.'
    else:
        return 'I didn\'t understand that. Please ask a different question.'
