from django.shortcuts import render, get_object_or_404
from .models import Counter
from django.shortcuts import redirect
from .forms import ItemForm
from .models import ItemInfo  # Update the import
from .forms import AddItemForm  # Import the new form
from django.contrib import messages  # Import messages to display flash messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Comment
from .forms import CommentForm
from googletrans import Translator
from translate import Translator
from googletrans import LANGUAGES



def home(request):
    return render(request, 'counter/home.html')


def list(request):
    items = ItemInfo.objects.all()
    return render(request, 'counter/list.html', {'items': items})



@csrf_exempt
def update_votes(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        item = ItemInfo.objects.get(pk=item_id)
        item.votes += 1
        item.save()
        return JsonResponse({'votes': item.votes})
    else:
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def add_comment(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        comment_text = request.POST.get('comment_text')

        item = get_object_or_404(ItemInfo, pk=item_id)

        comment = Comment.objects.create(item=item, text=comment_text)
        item.comments += 1
        item.save()

        return JsonResponse({'comment_text': comment_text, 'item_id': item_id})

    return JsonResponse({'error': 'Invalid request method'})

def item_detail(request, item_id):
    item = get_object_or_404(ItemInfo, pk=item_id)
    comments = Comment.objects.filter(item=item)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.item = item
            comment.save()
            item.comments += 1
            item.save()
            return redirect('item_detail', item_id=item_id)

    return render(request, 'counter/item_detail.html', {'item': item, 'comments': comments, 'form': form})




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
    

def translate_text(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        target_language = request.POST.get('target_language', 'en')  # Default to English

        try:
            # Initialize the Translator
            translator= Translator(to_lang=target_language)

            # Translate the text
            translation = translator.translate(text)
            translated_text = translation

            return JsonResponse({'translated_text': translated_text})

        except Exception as e:
            return JsonResponse({'error': str(e)})

    return JsonResponse({'error': 'Invalid request method'})

