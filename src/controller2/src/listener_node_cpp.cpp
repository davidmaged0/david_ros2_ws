#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp" 

class ListenerNode : public rclcpp::Node
{
public:
    ListenerNode() : Node("listener_node")
    {
        subscription_ = create_subscription<std_msgs::msg::String>(
            "topic", 10, [this](const std_msgs::msg::String::SharedPtr msg) {
                RCLCPP_INFO(this->get_logger(), "I heard: '%s'", msg->data.c_str());
            });
    }

private:
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<ListenerNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
