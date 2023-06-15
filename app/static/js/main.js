// Function to handle form submission for time audit
function submitTimeAuditForm(event) {
    event.preventDefault(); // Prevent form submission

    // Get the form inputs
    var activityInput = document.getElementById('activity-input').value;
    var timeInput = document.getElementById('time-input').value;
    var locationInput = document.getElementById('location-input').value;
    var distanceInput = document.getElementById('distance-input').value;

    // Perform any necessary calculations or validations

    // Display the submitted data or update the recommendations based on the time audit
    fetchActivityRecommendations();

    // Reset the form inputs
    document.getElementById('activity-input').value = '';
    document.getElementById('time-input').value = '';
    document.getElementById('location-input').value = '';
    document.getElementById('distance-input').value = '';
}

// Event listener for time audit form submission
var timeAuditForm = document.getElementById('time-audit-form');
timeAuditForm && timeAuditForm.addEventListener('submit', submitTimeAuditForm);

// Function to fetch and display activity recommendations based on the time audit
function fetchActivityRecommendations() {
    // Simulated example data
    var timeAuditData = [
        { activity: 'Walking', time: 30 },
        { activity: 'Reading', time: 60 },
        { activity: 'Chatting', time: 45 },
        { activity: 'Exercise', time: 90 },
    ];

    // Define the quadrants of the Eisenhower Matrix
    var importantUrgent = [];
    var importantNotUrgent = [];
    var notImportantUrgent = [];
    var notImportantNotUrgent = [];

    // Categorize the activities based on time audit
    timeAuditData.forEach(function (item) {
        if (item.time > 60) {
            if (item.activity === 'Exercise') {
                importantUrgent.push(item.activity);
            } else {
                importantNotUrgent.push(item.activity);
            }
        } else {
            if (item.activity === 'Chatting') {
                notImportantUrgent.push(item.activity);
            } else {
                notImportantNotUrgent.push(item.activity);
            }
        }
    });

    // Update the DOM with the fetched recommendations
    var recommendationsContainer = document.getElementById('recommendations');
    recommendationsContainer.innerHTML = '';

    var matrixHeading = document.createElement('h4');
    matrixHeading.textContent = 'Eisenhower Matrix Recommendations:';
    recommendationsContainer.appendChild(matrixHeading);

    // Create and append recommendation lists for each quadrant
    appendRecommendationsList(importantUrgent, 'Important & Urgent:', recommendationsContainer);
    appendRecommendationsList(importantNotUrgent, 'Important & Not Urgent:', recommendationsContainer);
    appendRecommendationsList(notImportantUrgent, 'Not Important & Urgent:', recommendationsContainer);
    appendRecommendationsList(notImportantNotUrgent, 'Not Important & Not Urgent:', recommendationsContainer);
}

// Function to create and append recommendation lists to the recommendations container
function appendRecommendationsList(recommendations, heading, container) {
    var recommendationsList = document.createElement('ul');
    var recommendationsHeading = document.createElement('h5');
    recommendationsHeading.textContent = heading;

    recommendations.forEach(function (recommendation) {
        var listItem = document.createElement('li');
        listItem.textContent = recommendation;
        recommendationsList.appendChild(listItem);
    });

    container.appendChild(recommendationsHeading);
    container.appendChild(recommendationsList);
}

// Function to handle recording of activity
function recordActivity() {
    var activityInput = document.getElementById('activity-input').value;
    var timeInput = document.getElementById('time-input').value;
    var locationInput = document.getElementById('location-input').value;
    var distanceInput = document.getElementById('distance-input').value;


    // Display a success message or update the recommendations based on the time audit
    var recommendationsContainer = document.getElementById('recommendations');
    recommendationsContainer.innerHTML = '<p>Activity recorded successfully!</p>';

    // Reset the form inputs
    document.getElementById('activity-input').value = '';
    document.getElementById('time-input').value = '';
    document.getElementById('location-input').value = '';
    document.getElementById('distance-input').value = '';
}

// Function to display the current activity prompt
function displayActivityPrompt(promptText) {
    var activityPromptElement = document.getElementById('current-activity-prompt');
    if (activityPromptElement) {
        activityPromptElement.textContent = 'Prompt: ' + promptText;
    }
}

// Function to generate a random activity prompt
function generateActivityPrompt() {
    var prompts = [
        'Stretch your legs and take a short walk.',
        'Do a quick set of jumping jacks.',
        'Take a moment to practice deep breathing.',
        'Stand up and stretch your arms and shoulders.',
        'Take a break and drink a glass of water.',
        'Listen to a favorite song and dance along.',
        'Practice a mindful meditation for a few minutes.',
    ];

    var randomIndex = Math.floor(Math.random() * prompts.length);
    var randomPrompt = prompts[randomIndex];

    displayActivityPrompt(randomPrompt);
}


generateActivityPrompt();

// Function to handle the click event for the "Record Activity" button
function handleClickRecordActivity() {
    recordActivity();
    generateActivityPrompt();
}

// Event listener for the "Record Activity" button
var recordActivityButton = document.getElementById('record-activity-btn');
recordActivityButton && recordActivityButton.addEventListener('click', handleClickRecordActivity);

