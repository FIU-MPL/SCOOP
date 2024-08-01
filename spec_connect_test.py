import seabreeze.spectrometers as sb

# Get a list of available spectrometers
devices = sb.list_devices()
print(devices)

if len(devices) == 0:
    print("No spectrometers found.")
else:
    # Connect to the first spectrometer (you can choose a specific device from the list)
    spectrometer = sb.Spectrometer(devices[0])

    # Acquire spectrum data
    spectrum = spectrometer.spectrum()

    # Print the spectrum data
    print("Wavelengths (nm):", spectrum.wavelengths())
    print("Intensity:", spectrum.intensities())

    # Close the spectrometer when done
    spectrometer.close()