
def overflow_preventer(container_height , window_height):
        if(container_height > 50 or window_height > 50):
            raise ValueError("container size is too big and has overflown Window due to number of widgets please reconfigure"
                             " amount of widgets within the container")
        else:
            return

