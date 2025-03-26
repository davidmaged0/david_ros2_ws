from launch import LaunchDescription
import launch.substitutions
import launch_ros.actions

def generate_launch_description():
    ld= LaunchDescription()
    talker_node = launch_ros.actions.Node(
        package="demo_nodes_cpp",
        executable="talker",
        #name='talker',
        #output='screen'
    )
    listener_node = launch_ros.actions.Node(
        package="demo_nodes_cpp",
        executable="listener",
        #name='listener',
        #output='screen'
    )



    ld.add_action(talker_node)
    ld.add_action(listener_node)


    return ld

