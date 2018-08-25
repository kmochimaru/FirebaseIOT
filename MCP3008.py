import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

#CLK = 18
#MISO = 23
#MOSI = 24
#CS = 25
#mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

while True:
	print(mcp.read_adc(7))
