const typewriterText = [
    "Recall before you resume reading.",
    "End any plot the way you desire.",
    "Get AI generated book recommedations."
  ];
  
  let currentTextIndex = 0;
  let currentText = "";
  let isDeleting = false;
  
  function type() {
    const currentIndex = currentTextIndex % typewriterText.length;
    const fullText = typewriterText[currentIndex];
  
    if (isDeleting) {
      currentText = fullText.substring(0, currentText.length - 1);
    } else {
      currentText = fullText.substring(0, currentText.length + 1);
    }
  
    document.getElementById("typewriter-text").innerText = currentText;
  
    let typingSpeed = 50;
    if (isDeleting) {
      typingSpeed /= 2;
    }
  
    if (!isDeleting && currentText === fullText) {
      typingSpeed = 1500;
      isDeleting = true;
    } else if (isDeleting && currentText === "") {
      isDeleting = false;
      currentTextIndex++;
      typingSpeed = 500;
    }
  
    setTimeout(type, typingSpeed);
  }
  
  document.addEventListener("DOMContentLoaded", () => {
    type();
  });

  

function showUploadForm() {
    const uploadForm = document.querySelector('.upload-form');
    uploadForm.style.display = 'block';
}

function submitForm() {
    // Add your logic here to handle form submission
    // For example, you can get the values of the inputs using document.getElementById().value
    // and perform any necessary actions with the data.
    // Once the form is submitted, you can hide the form again if needed.
    const uploadForm = document.querySelector('.upload-form');
    uploadForm.style.display = 'none';
}

// JavaScript to control the modal

// Get the modal element
const modal = document.getElementById('myModal');

// Get the button that opens the modal
const btn = document.querySelector('.upload-button');

// Get the <span> element that closes the modal
const closeBtn = document.querySelector('.close');

// Function to open the modal
function openModal() {
    modal.style.display = 'block';
}

// Function to close the modal
function closeModal() {
    modal.style.display = 'none';
}

// Attach event listeners to the button and close button
btn.addEventListener('click', openModal);
closeBtn.addEventListener('click', closeModal);

// When the user clicks outside the modal, close it
window.addEventListener('click', function(event) {
    if (event.target == modal) {
        closeModal();
    }
});

// JavaScript to control the modal for Recap a Podcast

// Get the modal element for Recap a Podcast
const modalPodcast = document.getElementById('myModalPodcast');

// Function to open the modal for Recap a Podcast
function showPodcastForm() {
    modalPodcast.style.display = 'block';
}

// Function to close the modal for Recap a Podcast
function closeModalPodcast() {
    modalPodcast.style.display = 'none';
}

// Attach event listener to the close button for Recap a Podcast
const closeBtnPodcast = document.querySelector('.close');
closeBtnPodcast.addEventListener('click', closeModalPodcast);

// When the user clicks outside the modal for Recap a Podcast, close it
window.addEventListener('click', function (event) {
    if (event.target == modalPodcast) {
        closeModalPodcast();
    }
});


// JavaScript to open the Recall Plot Points page in a new tab
function openRecallPlotPointsPage() {
  window.open('recall_plot.html', '_blank');
}







  
  