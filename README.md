# Curiosa

  A curiosity-driven amoeba agent that explores a 2D physics world with no external rewards — driven purely by intrinsic motivation. It absorbs objects to morph its body, changing its physical properties and forcing itself to relearn
  locomotion.

  ## TODO

  ### Phase 1: Physics Foundation
  - [ ] Basic pymunk space with gravity and a ball
  - [ ] Pygame rendering loop at 60fps
  - [ ] Keyboard-controlled forces (WASD) on the ball
  - [ ] Static terrain — floors, walls, ramps
  - [ ] Procedural terrain generation with noise functions
  - [ ] Camera that follows the player/agent

  ### Phase 2: Absorbable Objects
  - [ ] Base absorbable object class
  - [ ] Five object types (rock, elastic, slime, bubble, stick)
  - [ ] Scatter objects in the world via seeded noise
  - [ ] Collision detection between agent and objects
  - [ ] Object removal on absorption

  ### Phase 3: Morphing Agent
  - [ ] Soft-body circle (multiple pymunk bodies + spring joints)
  - [ ] Absorption mechanic — blend physics properties on contact
  - [ ] Body state encoding (mass, friction, restitution, radius, type histogram)
  - [ ] Visual changes on absorption (size, color tint)
  - [ ] Verify that movement feels different after absorption

  ### Phase 4: Gymnasium Environment
  - [ ] Wrap the world as a Gymnasium env (reset, step, observe)
  - [ ] Define observation space (47 floats)
  - [ ] Define action space (2D continuous — angle + magnitude)
  - [ ] Test with random actions

  ### Phase 5: ICM (Curiosity Engine)
  - [ ] Feature encoder network (MLP 128→128→64)
  - [ ] Forward model (predicts next features from current + action)
  - [ ] Inverse model (predicts action from state pair)
  - [ ] Combined loss function
  - [ ] Intrinsic reward = forward model prediction error
  - [ ] Reward normalization (running mean/std)

  ### Phase 6: PPO Training
  - [ ] Integrate Stable Baselines 3 PPO with custom env
  - [ ] Wire intrinsic reward from ICM as the only reward
  - [ ] Training loop with TensorBoard logging
  - [ ] Checkpoint save/load
  - [ ] YAML config for hyperparameters
  - [ ] Verify agent learns to move (not just flail)

  ### Phase 7: Visualization & Dashboard
  - [ ] Pygame renderer — color-coded objects, agent body changes
  - [ ] Curiosity overlay (glow on high-prediction-error areas)
  - [ ] Dash web dashboard — exploration heatmap
  - [ ] Curiosity signal graph (intrinsic reward over time)
  - [ ] Body composition timeline
  - [ ] Absorption log table

  ### Phase 8: Polish
  - [ ] Seed management for reproducibility
  - [ ] Experiment comparison across runs
  - [ ] Performance tuning for RTX 3050
  - [ ] Clean up and document config options