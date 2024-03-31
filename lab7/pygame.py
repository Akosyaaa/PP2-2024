#ex1
import os
import pygame
import datetime

desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

bg_path = os.path.join(desktop_path, "main-clock.png")
r_hand_path = os.path.join(desktop_path, "right-hand.png")
l_hand_path = os.path.join(desktop_path, "left-hand.png")

pygame.init()
screen = pygame.display.set_mode((1400, 1050), pygame.RESIZABLE)
done = True
bg = pygame.image.load(bg_path)
r_hand = pygame.image.load(r_hand_path)
l_hand = pygame.image.load(l_hand_path)

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    now = datetime.datetime.now()
    min_angle = now.minute * 6
    sec_angle = now.second * 6
    rot_r_hand = pygame.transform.rotate(r_hand, -min_angle)
    rot_l_hand = pygame.transform.rotate(l_hand, -sec_angle)

    screen.blit(bg, (0, 0))
    screen.blit(rot_r_hand, rot_r_hand.get_rect(center=(700, 525)))
    screen.blit(rot_l_hand, rot_l_hand.get_rect(center=(700, 525)))

    pygame.display.update()

pygame.quit()