import pymunk
import pygame

# Physics setup
space = pymunk.Space()
space.gravity = (0, 500)  # gravity pulls down

# Create a ball
mass = 1
radius = 20
body = pymunk.Body(mass, pymunk.moment_for_circle(mass, 0, radius))
body.position = (400, 100)  # start near top
shape = pymunk.Circle(body, radius)
shape.elasticity = 0.8
shape.friction = 0.5
space.add(body, shape)

# Create a floor
floor_body = pymunk.Body(body_type=pymunk.Body.STATIC)
floor_shape = pymunk.Segment(floor_body, (0, 500), (800, 500), 5)
floor_shape.elasticity = 0.8
floor_shape.friction = 0.5
space.add(floor_body, floor_shape)

# Left wall
left_wall_body = pymunk.Body(body_type=pymunk.Body.STATIC)
left_wall_shape = pymunk.Segment(left_wall_body, (0, 0), (0, 600), 5)
left_wall_shape.elasticity = 0.8
left_wall_shape.friction = 0.5
space.add(left_wall_body, left_wall_shape)

# Right wall
right_wall_body = pymunk.Body(body_type=pymunk.Body.STATIC)
right_wall_shape = pymunk.Segment(right_wall_body, (800, 0), (800, 600), 5)
right_wall_shape.elasticity = 0.8
right_wall_shape.friction = 0.5
space.add(right_wall_body, right_wall_shape)

# Ramp
ramp_body = pymunk.Body(body_type=pymunk.Body.STATIC)
ramp_shape = pymunk.Segment(ramp_body, (100, 450), (400, 350), 5)
ramp_shape.elasticity = 0.5
ramp_shape.friction = 0.7
space.add(ramp_body, ramp_shape)

# Ledge
ledge_body = pymunk.Body(body_type=pymunk.Body.STATIC)
ledge_shape = pymunk.Segment(ledge_body, (500, 400), (700, 420), 5)
ledge_shape.elasticity = 0.5
ledge_shape.friction = 0.7
space.add(ledge_body, ledge_shape)

# Pygame rendering
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Curiosa — Physics Test")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Apply forces with keyboard
    keys = pygame.key.get_pressed()
    force = 500
    if keys[pygame.K_w]:
        body.apply_force_at_local_point((0, -force))
    if keys[pygame.K_s]:
        body.apply_force_at_local_point((0, force))
    if keys[pygame.K_a]:
        body.apply_force_at_local_point((-force, 0))
    if keys[pygame.K_d]:
        body.apply_force_at_local_point((force, 0))

    # Step physics
    space.step(1 / 60)

    # Draw
    screen.fill((20, 20, 30))

    # Draw terrain
    terrain_color = (100, 100, 120)
    ramp_color = (140, 120, 80)
    pygame.draw.line(screen, terrain_color, (0, 500), (800, 500), 5)      # floor
    pygame.draw.line(screen, terrain_color, (0, 0), (0, 600), 5)          # left wall
    pygame.draw.line(screen, terrain_color, (800, 0), (800, 600), 5)      # right wall
    pygame.draw.line(screen, ramp_color, (100, 450), (400, 350), 5)       # ramp
    pygame.draw.line(screen, ramp_color, (500, 400), (700, 420), 5)       # ledge

    # Draw ball
    pos = int(body.position.x), int(body.position.y)
    pygame.draw.circle(screen, (120, 200, 160), pos, radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()