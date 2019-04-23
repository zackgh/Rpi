int fortRead = A0;
int readValue;

void setup() {
  // put your setup code here, to run once:
  pinMode(fortRead,INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  readValue = analogRead(fortRead);
  Serial.println(readValue);
}
