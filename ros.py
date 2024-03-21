import rospy
from std_msgs.msg import String
from std_msgs.msg import Char

from std_msgs.msg import UInt8
from std_msgs.msg import UInt16
from std_msgs.msg import UInt32
from std_msgs.msg import UInt64
from std_msgs.msg import Int16
from std_msgs.msg import Int32
from std_msgs.msg import Int64
from std_msgs.msg import Float32
from std_msgs.msg import Float64

from std_msgs.msg import Bool

from sensor_msgs.msg import NavSatFix
from sensor_msgs.msg import BatteryState
from sensor_msgs.msg import Image
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import PointCloud2
from sensor_msgs.msg import LaserScan


class RosDataGenerator:
    def __init__(self):
        self._setup_publishers()
        rospy.init_node("ros_msgs_test")
        while not rospy.is_shutdown():
            self._publish_messages()

    def _setup_publishers(self):
        self._stringpub = rospy.Publisher("stringpub", String, queue_size=1)
        self._charpub = rospy.Publisher("charpub", Char, queue_size=1)
        self._uint8pub = rospy.Publisher("uint8pub", UInt8, queue_size=1)
        self._uint16pub = rospy.Publisher("uint16pub", UInt16, queue_size=1)
        self._uint32pub = rospy.Publisher("uint32pub", UInt32, queue_size=1)
        self._uint64pub = rospy.Publisher("uint64pub", UInt64, queue_size=1)
        self._int16pub = rospy.Publisher("int16pub", Int16, queue_size=1)
        self._int32pub = rospy.Publisher("int32pub", Int32, queue_size=1)
        self._int64pub = rospy.Publisher("int64pub", Int64, queue_size=1)
        self._float32pub = rospy.Publisher("float32pub", Float32, queue_size=1)
        self._float64pub = rospy.Publisher("float64pub", Float64, queue_size=1)
        self._boolpub = rospy.Publisher("boolpub", Bool, queue_size=1)
        self._navsatfixpub = rospy.Publisher("navsatfixpub", NavSatFix, queue_size=1)
        self._batterystatepub = rospy.Publisher(
            "batterystatepub", BatteryState, queue_size=1
        )
        self._imagepub = rospy.Publisher("imagepub", Image, queue_size=1)
        self._compressedimagepub = rospy.Publisher(
            "compressedimagepub", CompressedImage, queue_size=1
        )
        self._pointcloud2pub = rospy.Publisher(
            "poincloud2pub", PointCloud2, queue_size=1
        )
        self._laserscanpub = rospy.Publisher("laserscanpub", LaserScan, queue_size=1)

    def _publish_messages(self):
        self._stringpub.publish("this is string")
        self._charpub.publish(Char())
        self._uint8pub.publish(UInt8())
        self._uint16pub.publish(UInt16())
        self._uint32pub.publish(UInt32())
        self._uint64pub.publish(UInt64())
        self._int16pub.publish(Int16())
        self._int32pub.publish(Int32())
        self._int64pub.publish(Int64())
        self._float32pub.publish(Float32())
        self._float64pub.publish(Float64())
        self._boolpub.publish(Bool())
        self._navsatfixpub.publish(NavSatFix())
        self._batterystatepub.publish(BatteryState())
        self._imagepub.publish(Image())
        self._compressedimagepub.publish(CompressedImage())
        self._pointcloud2pub.publish(PointCloud2())
        self._laserscanpub.publish(LaserScan())


if __name__ == "__main__":
    ros_pub_node = RosDataGenerator()