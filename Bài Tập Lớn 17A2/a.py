import random
import csv
colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Pink", "Brown", "Black", "White"]
drawn_colors = set()
ball_counts = {"Red": 10, "Blue": 10, "Green": 10, "Yellow": 10, "Purple": 10, "Orange": 10, "Pink": 10, "Brown": 10, "Black": 10, "White": 10}

# Rút 1 bóng ngẫu nhiên
def drawn_ball():
    available_colors = [color for color in colors if ball_counts[color] > 0]
    drawn_color = random.choice(available_colors)
    ball_counts[drawn_color] -= 1
    return drawn_color

# Xác suất rút được bóng của một màu cụ thể
def calculate_probability(color):
    total_balls = sum(ball_counts.values())
    if total_balls == 0:
        return 0
    else:
        return ball_counts[color] / total_balls

# Hiển thị số lượng bóng còn lại trong hộp
def display_remaining_balls():
    return ball_counts

# Rút bóng 5 lần và kiểm tra kết quả
def play_game():
    draws = []
    
    for _ in range(5):
        drawn_color = drawn_ball()
        if drawn_color is None:
            break
        
        probability = calculate_probability(drawn_color)
        remaining_balls = display_remaining_balls()
        
        draws.append((drawn_color, probability, remaining_balls.copy()))
        
    return draws

def check_winner(draws):
    color_counts = {}
    
    for draw in draws:
        color = draw[0]
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1
    
    for count in color_counts.values():
        if count >= 3:
            return True
        
    return False

# Lưu kết quả
def save_file(draws, filename="draw_results.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Drawn Color", "Probability", "Remaining Balls"])
        
        for draw in draws:
            color, probability, remaining_balls = draw
            writer.writerow([color, probability, remaining_balls])

# Chạy game
draws = play_game()
is_winner = check_winner(draws)

if is_winner:
    print("Người chơi chiến thắng!")
else:
    print("Người chơi thua cuộc!")
save_file(draws)