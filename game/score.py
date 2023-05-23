from utils import WIDTH, GAME_FONT_BIG

class Score():
    def __init__(self):
        self.current_score = 0
        self.best_score = 0
        self.new_best_score_flag = False
        
    def load_best_score(self):
        try:
            with open("best_score.txt", "r") as file:
                self.best_score = int(float(file.read()))
        except FileNotFoundError:
            self.best_score = 0
        if (self.best_score < self.current_score):
            self.best_score = self.current_score
            with open("best_score.txt", "w") as file:
                file.write(str(self.best_score))            
            self.new_best_score_flag = True

    
    def update_current_score(self, height):
        if (height//500 > self.current_score):
            self.current_score = height//500

    def draw(self, window):
        text = GAME_FONT_BIG.render("Score: " + str(int(self.current_score)), True, (0, 0, 0))
        text_rect = text.get_rect(center=(WIDTH/2, 60))
        window.blit(text, text_rect)         


