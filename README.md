# Simulating the Path of a Model Rocket Through Turbulent Wind

### Intro

If you are a model rocket enthusiast (especially one who has to operate with limited launching space), you are probably very familiar with the anxious feeling of not knowing where your rocket will land after it parachutes down. Will it land where you launched it? Will it land on a nearby road and get hit by a moving car? Or will it land in the nearby trees which you’ll have to climb to retrieve it.

For our project, we are planning on simulating the displacement of a model rocket flying through wind and parachuting back down to the ground. As demonstrated in the previous paragraph, this simulation would be useful for model rocket enthusiasts, who wish to know how far away and in which direction their rocket will land so that they can set it up in a safe location and prevent losing their potentially expensive rocket.

Although we would have loved to simulate the flight path of a real rocket or spaceship, that task seemed a little too complex and unfeasible for such a short timeline, so we decided to go with something more manageable. That being said, this model still has plenty of complexity to it, and would be an interesting problem to model. The randomness in a wind environment, the thrust of the engine, the time at which the parachute opens, and the angle at which the rocket is launched, all add to the complexity of the model. 

### Model Description

As mentioned in the Introduction, the goal of our model is to simulate how a model rocket is displaced when launched through a wind environment. Our model is going to simulate the rocket moving through a 3 dimensional grid of wind vectors (each vector has an x, y, and z scalar). The rocket starts out at ground level in the middle of the wind grid (i.e. if the wind grid is 500x500x500 meters, the rocket will start out at 250,250,0). When the simulation starts, the rocket accelerates for a certain number of steps and then free flies through the grid of wind until it reaches its peak (it is being pulled down by gravity the entire time). Once the rocket begins to fall (vertical velocity passes a certain threshold), its parachute is deployed, and the rocket slowly coasts down to the ground. The entire time from the rocket free flying to landing on the ground, the rocket is accelerated by the current closest wind vector in the environment. We will be measuring the displacement of the rocket from its launch point after it lands back onto the ground.
