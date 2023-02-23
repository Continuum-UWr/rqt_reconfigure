#!/usr/bin/env python3
import rclpy
import rclpy.node

from rcl_interfaces.msg import FloatingPointRange, IntegerRange, ParameterDescriptor, ParameterType

class ParamTest(rclpy.node.Node):
    def __init__(self):
        super().__init__("param_test_node")

        # BOOL -----------------------------
        # bool, not read only, not dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_BOOL, read_only=False, dynamic_typing=False)
        self.declare_parameter("bool_param", False, descriptor=desc)
        # bool, not read_only, dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_BOOL, read_only=False, dynamic_typing=True)
        self.declare_parameter("bool_param_dynamic_type", True, descriptor=desc)
        # bool, read only, not dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_BOOL, read_only=True, dynamic_typing=False)
        self.declare_parameter("bool_param_ro", False, descriptor=desc)
        # bool, read only, dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_BOOL, read_only=True, dynamic_typing=True)
        self.declare_parameter("bool_param_ro_dynamic_type", False, descriptor=desc)
        
        # BOOL ARAY ----------------------------------
        # bool arr, not read only, not dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_BOOL_ARRAY, read_only=False, dynamic_typing=False)
        self.declare_parameter("bool_arr_param", [False, False], descriptor=desc)
        # bool arr, not read_only, dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_BOOL_ARRAY, read_only=False, dynamic_typing=True)
        self.declare_parameter("bool_arr_param_dynamic_type", [True, False], descriptor=desc)
        # bool arr, read only, not dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_BOOL_ARRAY, read_only=True, dynamic_typing=False)
        self.declare_parameter("bool_arr_param_ro", [False, False], descriptor=desc)
        # bool arr, read only, dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_BOOL_ARRAY, read_only=True, dynamic_typing=True)
        self.declare_parameter("bool_arr_param_ro_dynamic_type", [False, False], descriptor=desc)
        
        # STRING -----------------------------
        # string, not read only, not dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_STRING, read_only=False, dynamic_typing=False)
        self.declare_parameter("string_param", "normal", descriptor=desc)
        # string, not read_only, dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_STRING, read_only=False, dynamic_typing=True)
        self.declare_parameter("string_param_dynamic_type", "dynamic", descriptor=desc)
        # string, read only, not dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_STRING, read_only=True, dynamic_typing=False)
        self.declare_parameter("string_param_ro", "ro", descriptor=desc)
        # string, read only, dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_STRING, read_only=True, dynamic_typing=True)
        self.declare_parameter("string_param_ro_dynamic_type", "dynamic ro", descriptor=desc)
        
        # STRING ARRAY -----------------------------
        # string arr, not read only, not dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_STRING_ARRAY, read_only=False, dynamic_typing=False)
        self.declare_parameter("string_arr_param", ["normal", "param"], descriptor=desc)
        # string arr, not read_only, dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_STRING_ARRAY, read_only=False, dynamic_typing=True)
        self.declare_parameter("string_arr_param_dynamic_type", ["dynamic", "param"], descriptor=desc)
        # string arr, read only, not dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_STRING_ARRAY, read_only=True, dynamic_typing=False)
        self.declare_parameter("string_arr_param_ro", ["read", "only"], descriptor=desc)
        # string arr, read only, dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_STRING_ARRAY, read_only=True, dynamic_typing=True)
        self.declare_parameter("string_arr_param_ro_dynamic_type", ["dynamic",  "read", "only"], descriptor=desc)

        # INTEGEER ---------------------------------------------------------------
        # int, no interval, not read only, not dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_INTEGER, read_only=False, dynamic_typing=False)
        self.declare_parameter("int_param", 1, descriptor=desc)
        # int, no interval, not read_only, dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_INTEGER, read_only=False, dynamic_typing=True)
        self.declare_parameter("int_param_dynamic_type", 2, descriptor=desc)
        # int, no interval, read only, not dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_INTEGER, read_only=True, dynamic_typing=False)
        self.declare_parameter("int_param_ro", 3, descriptor=desc)
        # int, no interval, read only, dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_INTEGER, read_only=True, dynamic_typing=True)
        self.declare_parameter("int_param_ro_dynamic_type", 4, descriptor=desc)
        
        int_interval=IntegerRange(from_value=-10, to_value=10, step=1)
        # int, interval, not read only, not dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_INTEGER, read_only=False, dynamic_typing=False, integer_range=[int_interval])
        self.declare_parameter("range_int_param", 1, descriptor=desc)
        # int, interval, not read_only, dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_INTEGER, read_only=False, dynamic_typing=True, integer_range=[int_interval])
        self.declare_parameter("range_int_param_dynamic_type", 2, descriptor=desc)
        # int, interval, read only, not dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_INTEGER, read_only=True, dynamic_typing=False, integer_range=[int_interval])
        self.declare_parameter("range_int_param_ro", 3, descriptor=desc)
        # int, interval, read only, dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_INTEGER, read_only=True, dynamic_typing=True, integer_range=[int_interval])
        self.declare_parameter("range_int_param_ro_dynamic_type", 4, descriptor=desc)

        # INTEGEER ARRAY ---------------------------------------------------------------
        # int arr, not read only, not dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_INTEGER_ARRAY, read_only=False, dynamic_typing=False)
        self.declare_parameter("int_arr_param", [1, 3, 7, 2], descriptor=desc)
        # int, not read_only, dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_INTEGER_ARRAY, read_only=False, dynamic_typing=True)
        self.declare_parameter("int_arr_param_dynamic_type", [2, 1, 3, 7], descriptor=desc)
        # int, read only, not dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_INTEGER_ARRAY, read_only=True, dynamic_typing=False)
        self.declare_parameter("int_arr_param_ro", [3, 7, 2, 1], descriptor=desc)
        # int, read only, dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_INTEGER_ARRAY, read_only=True, dynamic_typing=True)
        self.declare_parameter("int_arr_param_ro_dynamic_type", [7, 2, 1, 3], descriptor=desc)

        # DOUBLE
        # double, not interval, not read only, not dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_DOUBLE, read_only=False, dynamic_typing=False)
        self.declare_parameter("double_param", 1.0, descriptor=desc)
        # double, not interval, not read_only, dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_DOUBLE, read_only=False, dynamic_typing=True)
        self.declare_parameter("double_param_dynamic_type", 2.0, descriptor=desc)
        # double, not interval, read only, not dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_DOUBLE, read_only=True, dynamic_typing=False)
        self.declare_parameter("double_param_ro", 3.0, descriptor=desc)
        # double, interval, read only, dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_DOUBLE, read_only=True, dynamic_typing=True)
        self.declare_parameter("double_param_ro_dynamic_type", 4.0, descriptor=desc)

        float_interval = FloatingPointRange(from_value=-1.0, to_value=1.0, step=0.1)
        # double, interval, not read only, not dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_DOUBLE, read_only=False, dynamic_typing=False, floating_point_range=[float_interval])
        self.declare_parameter("range_double_param", 0.0, descriptor=desc)
        # double, interval, not read_only, dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_DOUBLE, read_only=False, dynamic_typing=True, floating_point_range=[float_interval])
        self.declare_parameter("range_double_param_dynamic_type", 0.0, descriptor=desc)
        # double, interval, read only, not dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_DOUBLE, read_only=True, dynamic_typing=False, floating_point_range=[float_interval])
        self.declare_parameter("range_double_param_ro", 0.0, descriptor=desc)
        # double, interval, read only, dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_DOUBLE, read_only=True, dynamic_typing=True, floating_point_range=[float_interval])
        self.declare_parameter("range_double_param_ro_dynamic_type", 0.0, descriptor=desc)

        # DOUBLE ARRAY
        # double arr, not interval, not read only, not dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_DOUBLE_ARRAY, read_only=False, dynamic_typing=False)
        self.declare_parameter("double_arr_param", [1.0], descriptor=desc)
        # double arr, not interval, not read_only, dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_DOUBLE_ARRAY, read_only=False, dynamic_typing=True)
        self.declare_parameter("double_arr_param_dynamic_type", [2.0], descriptor=desc)
        # double arr, not interval, read only, not dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_DOUBLE_ARRAY, read_only=True, dynamic_typing=False)
        self.declare_parameter("double_arr_param_ro", [3.0], descriptor=desc)
        # double, interval, read only, dynamic type
        desc = ParameterDescriptor(type=ParameterType.PARAMETER_DOUBLE_ARRAY, read_only=True, dynamic_typing=True)
        self.declare_parameter("double_arr_param_ro_dynamic_type", [4.0], descriptor=desc)

        # BYTE ARRAY
        # byte, not interval, not read only, not dynamic type
        # desc = ParameterDescriptor(type=ParameterType.PARAMETER_BYTE_ARRAY, read_only=False, dynamic_typing=False)
        # self.declare_parameter("byte_arr_param", descriptor=desc)
        # # byte, not interval, not read_only, dynamic type
        # desc = ParameterDescriptor(type=ParameterType.PARAMETER_BYTE_ARRAY, read_only=False, dynamic_typing=True)
        # self.declare_parameter("byte_arr_param_dynamic_type", descriptor=desc)
        # # byte, not interval, read only, not dynamic type
        # desc = ParameterDescriptor(type=ParameterType.PARAMETER_BYTE_ARRAY, read_only=True, dynamic_typing=False)
        # self.declare_parameter("byte_arr_param_ro", descriptor=desc)
        # # byte, interval, read only, dynamic type
        # desc = ParameterDescriptor(type=ParameterType.PARAMETER_BYTE_ARRAY, read_only=True, dynamic_typing=True)
        # self.declare_parameter("byte_arr_param_ro_dynamic_type", descriptor=desc)

        self.timer = self.create_timer(5, self.timer_callback)

    def timer_callback(self):
        my_param = self.get_parameter('int_param')
        param_val = my_param.get_parameter_value().integer_value

        self.get_logger().info(f"{param_val}")

        # my_new_param = rclpy.parameter.Parameter(
            # 'my_parameter',
            # rclpy.Parameter.Type.STRING,
            # 'world'
        # )
        # all_new_parameters = [my_new_param]
        my_param._value += 1
        self.set_parameters([my_param])

def main():
    rclpy.init()
    node = ParamTest()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
