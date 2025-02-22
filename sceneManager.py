import pygame
from settings import *

class SceneManager:
    def __init__(self):
        self.font = pygame.font.Font('freesansbold.ttf', 16)
        # self.messages = ["How can I be of assistance?",
        #                  "Is there some questions you would like to ask me?",
        #                  "If so go ahead and start asking."]
        self.answerOneMessage = "I am Burgermeister's daughter and care taker. I maintain all of his communications and schedule his appointments."
        self.answerTwoMessage = "I entered Burgermeister's room in the morning to wake him and noticed he was not in his room."
        self.snip = self.font.render('', True, 'white')
        self.counterOne = 0
        self.counterTwo = 0
        self.speed = 3
        self.active_message = 0
        # self.message = self.messages[self.active_message]
        self.done = False
        self.run = True

    def displayAnswerText(self, screen, question):
        keys = pygame.key.get_pressed()
        pygame.draw.rect(screen, 'black', [ANSWER_X, ANSWER_Y, ANSWER_WIDTH, ANSWER_HEIGHT])
        
        if question == 1:
            self.counterTwo = 0
            if self.counterOne < self.speed * len(self.answerOneMessage):
                self.counterOne += 1

            elif self.counterOne >= self.speed * len(self.answerOneMessage):
                self.done = True
        elif question == 2:
            self.counterOne = 0
            if self.counterTwo < self.speed * len(self.answerTwoMessage):
                self.counterTwo += 1

            elif self.counterTwo >= self.speed * len(self.answerTwoMessage):
                self.done = True

        # // division to the floor
        if question == 1:
            self.snip = self.font.render(self.answerOneMessage[0:self.counterOne//self.speed], True, 'white')
            # screen.blit(self.snip, (ANSWER_ONE_X+10, ANSWER_ONE_Y+10))
        elif question == 2:
            self.snip = self.font.render(self.answerTwoMessage[0:self.counterTwo//self.speed], True, 'white')
            # screen.blit(self.snip, (ANSWER_TWO_X+10, ANSWER_TWO_Y+10))

        screen.blit(self.snip, (ANSWER_X+10, ANSWER_Y+10))

    def update(self):
        self.displayAnswerText()
        
