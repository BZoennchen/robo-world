Disable the expensive Visualization
================================================

If students solve more complex problems they will eventually move ``Robo`` alot.
To animate the actions of ``Robo`` we basically copy the whole world in its current state.
This can lead to large memory requirements and can drastically influence computation times.
Therefore it is recommended to deactive the recording of the actions and/or the printing of each action.


Control the Printing
----------------------------

.. autofunction:: roboworld.Robo.disable_print

.. autofunction:: roboworld.Robo.enable_print


Control the Recording
----------------------------

.. autofunction:: roboworld.World.pause_recordings

.. autofunction:: roboworld.World.resume_recordings

.. autofunction:: roboworld.World.clear_recordings

.. autofunction:: roboworld.World.disable_animation

.. autofunction:: roboworld.World.enable_animation