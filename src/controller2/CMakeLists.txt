cmake_minimum_required(VERSION 3.8)
project(controller2)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()



add_executable(talker_node_cpp /home/david/david_ros2_ws/src/controller2/src/talker_node_cpp.cpp)
add_executable(listener_node_cpp /home/david/david_ros2_ws/src/controller2/src/listener_node_cpp.cpp)

ament_target_dependencies(talker_node_cpp rclcpp std_msgs)
ament_target_dependencies(listener_node_cpp rclcpp std_msgs)

install(TARGETS
  talker_node_cpp
  listener_node_cpp
  DESTINATION lib/${PROJECT_NAME})



ament_package()
