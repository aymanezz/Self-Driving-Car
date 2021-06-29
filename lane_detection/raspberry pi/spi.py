import spidev

spi_bus = 0
spi_device = 0

spi = spidev.SpiDev()

spi.open(spi_bus, spi_device)
spi.max_speed_hz = 1000000

send_byte = 0
spi.xfer2([send_byte])