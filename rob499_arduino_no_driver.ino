#include <micro_ros_arduino.h>
#include <rcl/rcl.h>
#include <rclc/rclc.h>
#include <std_msgs/msg/int32.h>
#include <std_msgs/msg/int32_multi_array.h>
#include <ESP32Servo.h>
#include <LiquidCrystal.h>
#include <Keypad.h>

LiquidCrystal lcd(27,26,25,33,32,14);

const byte ROWS=4,COLS=4;
char keys[ROWS][COLS]={{'1','2','3','A'},{'4','5','6','B'},{'7','8','9','C'},{'*','0','#','D'}};
byte rowPins[ROWS]={4,5,18,19}, colPins[COLS]={2,15,13,12};
Keypad keypad(makeKeymap(keys),rowPins,colPins,ROWS,COLS);

Servo fingers[5];
int servoPins[5]={21,16,17,23,22};
int currentPos[5];

rcl_publisher_t pub;
rcl_subscription_t sub;
std_msgs__msg__Int32 req_msg;
std_msgs__msg__Int32MultiArray pos_msg;
rclc_executor_t executor;
rcl_node_t node;
rclc_support_t support;
rcl_allocator_t allocator;

void pos_callback(const void * msgin)
{
  const auto * m = (const std_msgs__msg__Int32MultiArray *)msgin;
  for(int i=0;i<5 && i<m->data.size;i++){
    int angle=m->data.data[i];
    fingers[i].write(angle);
  }
}

void setup() {
  Serial.begin(115200);
  set_microros_transports();
  allocator = rcl_get_default_allocator();
  rclc_support_init(&support,0,NULL,&allocator);
  rclc_node_init_default(&node,"esp32_node","","",&support);
  rclc_publisher_init_default(&pub,&node,
    ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs,msg,Int32),"position_request");
  rclc_subscription_init_default(&sub,&node,
    ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs,msg,Int32MultiArray),"servo_positions",RCL_MEM_S_HISTORY_KEEP_LAST,10);
  rclc_executor_init(&executor,&support.context,1,&allocator);
  rclc_executor_add_subscription(&executor,&sub,&pos_msg,pos_callback,ON_NEW_DATA);

  lcd.begin(16,2);
  lcd.print("Ready");
  for(int i=0;i<5;i++){
    fingers[i].setPeriodHertz(50);
    fingers[i].attach(servoPins[i],500,2400);
    fingers[i].write(0);
  }
}

void loop() {
  rclc_executor_spin_some(&executor,RCL_MS_TO_NS(10));
  char k=keypad.getKey();
  if(k>='1' && k<='9'){
    lcd.clear(); lcd.print("Position "); lcd.print(k);
    req_msg.data=k-'0';
    rcl_publish(&pub,&req_msg,NULL);
    delay(100);
  }
}
