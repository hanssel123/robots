import rospy
from sensor_msgs.msg import PointCloud2, PointField
import std_msgs.msg
import numpy as np


def generate_point_cloud():
    # Create a ROS node
    rospy.init_node("point_cloud_publisher", anonymous=True)

    # Define the publishers
    pub1 = rospy.Publisher("point_cloud_topic1", PointCloud2, queue_size=10)
    pub2 = rospy.Publisher("point_cloud_topic2", PointCloud2, queue_size=10)
    pub3 = rospy.Publisher("point_cloud_topic3", PointCloud2, queue_size=10)
    pub4 = rospy.Publisher("point_cloud_topic4", PointCloud2, queue_size=10)
    pub5 = rospy.Publisher("point_cloud_topic5", PointCloud2, queue_size=10)

    # Set the publishing rate (in Hz)
    rate = rospy.Rate(50)

    while not rospy.is_shutdown():
        for topic_id in range(1, 6):
            # Create a new PointCloud2 message
            point_cloud_msg = PointCloud2()

            # Generate unique point cloud data for each topic
            point_cloud_data = generate_unique_data(topic_id)

            # Populate the header of the PointCloud2 message
            point_cloud_msg.header = std_msgs.msg.Header()
            point_cloud_msg.header.stamp = rospy.Time.now()
            point_cloud_msg.header.frame_id = "base"

            # Populate the point cloud data fields
            point_cloud_msg.height = 1
            point_cloud_msg.width = point_cloud_data.shape[0]

            fields = [
                PointField(name="x", offset=0, datatype=PointField.FLOAT32, count=1),
                PointField(name="y", offset=4, datatype=PointField.FLOAT32, count=1),
                PointField(name="z", offset=8, datatype=PointField.FLOAT32, count=1),
            ]

            point_cloud_msg.fields = fields
            point_cloud_msg.is_bigendian = False
            point_cloud_msg.point_step = 12
            point_cloud_msg.row_step = (
                point_cloud_msg.point_step * point_cloud_msg.width
            )
            point_cloud_msg.is_dense = False
            point_cloud_msg.data = point_cloud_data.tostring()

            # Publish the point cloud on the corresponding topic
            if topic_id == 1:
                pub1.publish(point_cloud_msg)
            elif topic_id == 2:
                pub2.publish(point_cloud_msg)
            elif topic_id == 3:
                pub3.publish(point_cloud_msg)
            elif topic_id == 4:
                pub4.publish(point_cloud_msg)
            elif topic_id == 5:
                pub5.publish(point_cloud_msg)

        rate.sleep()


def generate_unique_data(topic_id):
    # Generate unique point cloud data based on the topic ID
    num_points = 1000

    if topic_id == 5:
        x_offset = 0.0
        y_offset = 0.0

        # Higher z-coordinate for the fifth point cloud
        z_offset = 10.0
    else:
        # Different quadrants for the x-y plane based on the topic ID
        x_offset = 0.0
        y_offset = 0.0

        if topic_id == 1:
            x_offset = -5.0
            y_offset = -5.0
        elif topic_id == 2:
            x_offset = -5.0
            y_offset = 5.0
        elif topic_id == 3:
            x_offset = 5.0
            y_offset = -5.0
        elif topic_id == 4:
            x_offset = 5.0
            y_offset = 5.0

        z_offset = 0.0

    # Generate point cloud data with unique locations
    x = np.random.uniform(-2, 2, num_points) + x_offset
    y = np.random.uniform(-2, 2, num_points) + y_offset
    z = np.random.uniform(0, 0.1, num_points) + z_offset
    point_cloud_data = np.column_stack((x, y, z)).astype(np.float32)

    return point_cloud_data


if __name__ == "__main__":
    try:
        generate_point_cloud()
    except rospy.ROSInterruptException:
        pass
