import psutil
import pynvml

# Set the temperature thresholds
cpu_threshold = 90  # CPU temperature threshold in degrees Celsius
gpu_threshold = 90  # GPU temperature threshold in degrees Celsius

def get_cpu_temperature():
    try:
        # Get the current CPU temperature (works on some systems)
        return psutil.sensors_temperatures()['coretemp'][0].current
    except Exception as e:
        print(f"Failed to get CPU temperature: {e}")
        return None

def get_gpu_temperature():
    try:
        # Initialize NVML
        pynvml.nvmlInit()
        handle = pynvml.nvmlDeviceGetHandleByIndex(0)  # Assuming the first GPU is used
        gpu_temperature = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)
        return gpu_temperature
    except Exception as e:
        print(f"Failed to get GPU temperature: {e}")
        return None

while True:
    # Get CPU and GPU temperatures
    cpu_temp = get_cpu_temperature()
    gpu_temp = get_gpu_temperature()

    if cpu_temp is not None:
        print(f"CPU Temperature: {cpu_temp}°C")
        if cpu_temp >= cpu_threshold:
            # Execute actions for high CPU temperature
            print("CPU temperature exceeded the threshold! Taking action...")
            # Add your actions here

    if gpu_temp is not None:
        print(f"GPU Temperature: {gpu_temp}°C")
        if gpu_temp >= gpu_threshold:
            # Execute actions for high GPU temperature
            print("GPU temperature exceeded the threshold! Taking action...")
            # Add your actions here

    # Sleep for a while before checking temperatures again
    import time
    time.sleep(60)  # Sleep for 60 seconds (adjust as needed)
