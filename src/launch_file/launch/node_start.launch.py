from launch import LaunchDescription
import launch.substitutions
import launch_ros.actions

def generate_launch_description():
    ld= LaunchDescription()
    talker_node = launch_ros.actions.Node(
        package="my_robot_controller",
        executable="test_node",
        #name='talker',
        #output='screen'
    )
    listener_node = launch_ros.actions.Node(
        package="turtlesim",
        executable="turtlesim_node",
        #name='listener',
        output='screen'
    )



    ld.add_action(talker_node)
    ld.add_action(listener_node)


    return ld

