const startButton = document.getElementById('start-btn')
const nextButton = document.getElementById('next-btn')
const questionContainerElement = document.getElementById('question-container')
const questionElement = document.getElementById('question')
const answerButtonsElement = document.getElementById('answer-buttons')

let shuffledQuestions, currentQuestionIndex

startButton.addEventListener('click', startGame)
nextButton.addEventListener('click', () => {
  currentQuestionIndex++
  setNextQuestion()
})

function startGame() {
  startButton.classList.add('hide')
  shuffledQuestions = questions.sort(() => Math.random() - .5)
  currentQuestionIndex = 0
  questionContainerElement.classList.remove('hide')
  setNextQuestion()
}

function setNextQuestion() {
  resetState()
  showQuestion(shuffledQuestions[currentQuestionIndex])
}

function showQuestion(question) {
  questionElement.innerText = question.question
  question.answers.forEach(answer => {
    const button = document.createElement('button')
    button.innerText = answer.text
    button.classList.add('btn')
    if (answer.correct) {
      button.dataset.correct = answer.correct
    }
    button.addEventListener('click', selectAnswer)
    answerButtonsElement.appendChild(button)
  })
}

function resetState() {
  clearStatusClass(document.body)
  nextButton.classList.add('hide')
  while (answerButtonsElement.firstChild) {
    answerButtonsElement.removeChild(answerButtonsElement.firstChild)
  }
}

function selectAnswer(e) {
  const selectedButton = e.target
  const correct = selectedButton.dataset.correct
  setStatusClass(document.body, correct)
  Array.from(answerButtonsElement.children).forEach(button => {
    setStatusClass(button, button.dataset.correct)
  })
  if (shuffledQuestions.length > currentQuestionIndex + 1) {
    nextButton.classList.remove('hide')
  } else {
    startButton.innerText = 'Restart'
    startButton.classList.remove('hide')
  }
}

function setStatusClass(element, correct) {
  clearStatusClass(element)
  if (correct) {
    element.classList.add('correct')
  } else {
    element.classList.add('wrong')
  }
}

function clearStatusClass(element) {
  element.classList.remove('correct')
  element.classList.remove('wrong')
}

const questions = [
  {
    question: 'Who is St. Patrick?',
    answers: [
      { text: 'Famous Leprechaun', correct: false },
      { text: 'Saint of Ireland ', correct: true },
      { text: 'A jolly green man', correct: false},
      { text: 'Apostle', correct: false}
    ]
  },
  {
    question: 'When is St Patricks day?',
    answers: [
      { text: '17th of March', correct: true },
      { text: 'Everyday', correct: false },
      { text: '25th of December', correct: false },
      { text: '17th of April', correct: false }
    ]
  },
  {
    question: 'What miracles did St. Patrick Perform?',
    answers: [
      { text: 'Gathered all the snake in Ireland', correct: false },
      { text: 'Banished all the snaked from Ireland', correct: true },
      { text: 'Walked on water', correct: false },
      { text: 'IDK', correct: false }
    ]
  },
  {
    question: 'What is the colour of St. Patricks day?',
    answers: [
      { text: 'Red', correct: false },
      { text: 'Green', correct: true }
    ]
  }
]