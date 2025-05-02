const chatBox = 
    document.getElementById('chat-box');
const userInput = 
    document.getElementById('user-input');
const sendButton = 
    document.getElementById('send-button');
const sidebarToggle = 
    document.getElementById('sidebar-toggle');
const modeToggle = 
    document.getElementById('mode-toggle-checkbox');
const sidebar = 
    document.querySelector('.sidebar');

modeToggle.addEventListener('change', () => {
    document.body.classList.toggle('dark-mode');
});

sendButton.addEventListener('click', sendMessage);
userInput.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        sendMessage();
    }
});

document.addEventListener('DOMContentLoaded', function () {
    const newConversationBtn = 
            document.getElementById('new-conversation-btn');
    const conversationContent = 
            document.querySelector('.conversation-content');
    const sidebarToggle = 
            document.getElementById('sidebar-toggle');
    const chatContainer = 
            document.querySelector('.chat-container');

    sidebarToggle.addEventListener('click', function () {
        const sidebar = document.querySelector('.sidebar');
        sidebar.classList.toggle('collapsed');

        if (sidebar.classList.contains('collapsed')) {
            chatContainer.style.width = '96%';
            chatContainer.style.marginLeft = '3%';
        } else {
            chatContainer.style.width = 'calc(100% - 300px)';
            chatContainer.style.marginLeft = '300px';
        }
    });
    newConversationBtn.addEventListener('click', function () {
        conversationContent.textContent = "New Conversation Started!";
    });

    modeToggleCheckbox.addEventListener('change', function () {
        chatContainer.classList.toggle('light-mode');
        chatContainer.classList.toggle('dark-mode');
    });
});

function sendMessage() {
    const message = userInput.value.trim();
    if (message !== '') {
        appendMessage('user', message);
        getResponse(message);
        userInput.value = '';
    }
}

function appendMessage(sender, message) {
    const p = document.createElement('p');
    p.textContent = `${sender}: ${message}`;
    chatBox.appendChild(p);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function getResponse(message) {
    let response;
    const greetings = 
        ["Hello!", "Hi there!", "Hey!", "Greetings!"];
    const affirmatives = 
        ["Yes", "Certainly", "Of course", "Absolutely"];
    const negatives = 
        ["No", "Sorry, I can't do that", "Unfortunately not", "I'm afraid not"];
    const thanks = 
        ["You're welcome!", "No problem!", "Glad to help!", "Anytime!"];
    const commands = {
        "help": "You can ask me questions or chat about various topics.",
        "time": getCurrentTime(),
        "date": getCurrentDate(),
        "weather": getWeatherInfo(),
        "joke": getJoke(),
        "fact": getFact(),
        "quote": getQuote(),
        
        // Add more commands here as needed
    };

    if (message.toLowerCase() in commands) {
        response = commands[message.toLowerCase()];
    } else if (message.toLowerCase().includes("thank")) {
        response = getRandomElement(thanks);
    } else if (message.toLowerCase().includes("yes")) {
        response = getRandomElement(affirmatives);
    } else if (message.toLowerCase().includes("no")) {
        response = getRandomElement(negatives);
    } else {
        response = getRandomElement(greetings);
    }

    setTimeout(() => appendMessage('ChatGPT', response), 1000);
}

function getCurrentTime() {
    const now = new Date();
    return `Current time is ${now.toLocaleTimeString()}`;
}

function getCurrentDate() {
    const now = new Date();
    return `Today's date is ${now.toDateString()}`;
}

function getWeatherInfo() {

    // Simulate getting weather information from an API
    const weatherData = {
        temperature: getRandomNumber(10, 35),
        condition: getRandomElement(["Sunny", "Cloudy", "Rainy", "Windy"]),
    };
    return `Current weather: ${weatherData.temperature}°C,
                             ${weatherData.condition}`;
}

function getJoke() {
    
    // Simulate getting a random joke
    const jokes = ["Why don't scientists trust atoms? Because they make up everything!",
        "Parallel lines have so much in common. It's a shame they'll never meet.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"
    ];
    return getRandomElement(jokes);
}

function getFact() {
    
    // Simulate getting a random fact
    const facts = ["Ants stretch when they wake up in the morning.", 
                   "A group of flamingos is called a flamboyance.",
                   "Honey never spoils.",
                   "The shortest war in history lasted only 38 minutes.",
                   "Octopuses have three hearts."
    ];
    return getRandomElement(facts);
}

function getQuote() {
    
    // Simulate getting a random quote
    const quotes = 
        ["The only way to do great work is to love what you do. – Steve Jobs",
        "In the middle of difficulty lies opportunity. – Albert Einstein",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill"
    ];
    return getRandomElement(quotes);
}

function getRandomElement(array) {
    const randomIndex = Math.floor(Math.random() * array.length);
    return array[randomIndex];
}

function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
getResponse('Hello');
