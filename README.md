# BlotQuant

**Automated Western Blot densitometric analysis for protein quantification.**

BlotQuant is a Python-based application designed for the analysis of Western Blot images, specifically focusing on the determination of band intensities, background subtraction, and normalization. It features an intuitive user interface and supports various image formats including TIF, PNG, and JPG.

## Features

- **Automated Analysis:** Calculates band intensities, fold changes, and statistical significance.
- **Broad File Support:** Supports TIF, PNG, JPG, and other common image formats via OpenCV.
- **ROI & Lane Management:**
    - **Interactive ROI:** Draw and resize regions of interest around protein bands.
    - **Dynamic Separators:** Automatically split ROIs into lanes based on replicate count.
    - **Manual Adjustment:** Drag separators to precisely align with band positions.
- **Rotation Alignment:** Interactive slider to rotate blots for perfect vertical alignment.
- **Normalization:** Automatically normalize target proteins against loading controls (e.g., Actin, GAPDH).
- **Data Export:** Export comprehensive results to Excel or open data directly in GraphPad Prism.
- **Visual Feedback:** Real-time overlay of selected regions and lane dividers.

## Methods

BlotQuant employs a robust image processing pipeline to quantify protein bands:

### 1. Preprocessing
The application converts the input image to grayscale for intensity analysis. To ensure accurate lane separation, users can apply **Rotation Alignment** (using BICUBIC interpolation). This step is crucial for aligning bands vertically, which simplifies the subsequent lane division and prevents signal overlap between adjacent samples.

### 2. ROI Selection
Users define a Region of Interest (ROI) that encompasses all bands of a specific protein across multiple lanes. This ROI can be dynamically resized and moved to perfectly frame the signal.

### 3. Lane Separation
Based on the defined **Replicate Count**, the ROI is divided into equal lanes. For experiments with "Equal N" settings, the software can automatically handle paired Control and Treatment groups within a single ROI selection. Draggable separators allow for manual fine-tuning if lane spacing is irregular.

### 4. Quantification
Once the lanes are defined, individual band intensities are calculated:
- **Background Subtraction:** A local background value is determined using the **Median Intensity** of the ROI.
- **Integrated Density:** For each lane, the software calculates the sum of `(Pixel Intensity - Background)` for all pixels above a dynamic threshold (Background + 0.5 * Standard Deviation). This ensures that only the actual protein signal is counted, while noise and background are excluded.
- **Inversion:** Supports "Invert Signal" for blots where bands are darker than the background (e.g., Ponceau S or Coomassie staining).

### 5. Normalization and Statistics
- **Normalization:** Target protein intensities are divided by their respective loading control intensities from the same lane.
- **Statistics:** Calculates average fold change, standard error of the mean (SEM), and performs a Student's t-test (unpaired) to determine statistical significance between Control and Treatment groups.

## Citation

Users are requested to cite **Hauffe et al. 2026 (Placeholder, i will update this once the paper is published)** when using BlotQuant.

## License
This project is licensed under the MIT License – see the LICENSE file for details.

## Credits

**Author:** Dr. Robert Hauffe

**Affiliation:**
`https://www.uni-potsdam.de/de/mem/index`  
University of Potsdam, Germany

## Build Instructions

To build the standalone executable from source, follow these steps:

1. **Install Dependencies:**
   Ensure you have Python installed, then install the required packages:
   ```bash
   pip install PySide6 opencv-python numpy pandas pillow matplotlib scipy xlsxwriter
   ```

2. **Run PyInstaller:**
   Use the following command to create the single-file executable (ensure `Blot.ico` is in the project root):
   ```bash
   pyinstaller --noconfirm --onefile --windowed --icon "Blot.ico" --add-data "Blot.ico;." --name "BlotQuant" main.py
   ```

## Current Build Details (2026-02-06)
- **Version:** 1.0
- **SHA-256 Checksum:** `65F747E02197243D1111656A8CC25F4C193ABE3077BFA86B491F6098293A24F6`

To verify the integrity of your `BlotQuant.exe`, you can run the following command in PowerShell:
```powershell
Get-FileHash -Path "BlotQuant.exe" -Algorithm SHA256
```

## License

This project is available for academic use under an MIT licence.
