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
    question: 'People traditionally wear green on St. Patrick`s Day to avoid what?',
    answers: [
      { text: 'Getting kissed', correct: false },
      { text: 'Getting pinched ', correct: true },
      { text: 'One year of bad luck', correct: false},
      { text: 'Getting mugged', correct: false}
    ]
  },
  {
    question: 'What nationality was St. Patrick?',
    answers: [
      { text: 'Irish', correct: false },
      { text: 'German', correct: false },
      { text: 'Scottish', correct: true },
      { text: 'British', correct: false }
    ]
  },
  {
    question: 'What did St. Patrick believe a shamrock represented?',
    answers: [
      { text: 'Good luck', correct: false },
      { text: 'Good fortune', correct: false },
      { text: 'The holy trinity', correct: true },
      { text: 'IDK', correct: false }
    ]
  },
  {
    question: 'Which U.S. city dyes its river green annually to celebrate St. Patrick`s Day?',
    answers: [
      { text: 'Boston', correct: false },
      { text: 'Detroid', correct: false },
      { text: 'New York City', correct: false },
      { text: 'Chicago', correct: true }
    ]
  },
    {
    question: 'According to myth, when is the best time to sneak up on a leprechaun?',
    answers: [
      { text: 'When he is taking a nap', correct: false },
      { text: 'When he is counting gold', correct: false },
      { text: 'While he is mending his shoes', correct: true },
      { text: 'During his supper', correct: false }
    ]
  },
  {
    question: 'What was St. Patrick`s given birth name?',
    answers: [
      { text: 'Maewyn Succat', correct: true },
      { text: 'Henry O Malley', correct: false },
      { text: 'Patrick O Riley', correct: false },
      { text: 'John Smith', correct: false }
    ]
  },
  {
      question: 'How many pints of Guinness are consumed worldwide on St. Patrick`s Day?',
    answers: [
      { text: '13 million', correct: true },
      { text: '10 million', correct: false },
      { text: '5 million', correct: false },
      { text: '8 million', correct: false }
    ]
  },
   {
      question: 'Where and when was the first St. Paddy’s Day parade in the United States?',
    answers: [
      { text: 'Boston in 1809', correct: false },
      { text: 'Providence, R.I., in 1898', correct: false },
      { text: 'New York in 1762', correct: true }
    ]
  },
    {
      question: 'How do Leprechauns earn their gold?',
    answers: [
      { text: 'Collecting teeth', correct: false },
      { text: 'Making shoes', correct: true },
      { text: 'Dancing', correct: false },
      { text: 'Picking pockets', correct: false }
    ]
  },
    {
      question: 'Saint Patrick`s Day commemorates the _____ of Saint Patrick.',
    answers: [
      { text: 'Birth', correct: true },
      { text: 'Coronation', correct: false },
      { text: 'Death', correct: true },
    ]
  },
    {
      question: 'How long was the world`s shortest Saint Patrick`s Day parade?',
    answers: [
      { text: '23 meters', correct: true },
      { text: '89 meters', correct: false },
      { text: '10 meters', correct: false },
      { text: '60 meters', correct: false }
    ]
  },

]