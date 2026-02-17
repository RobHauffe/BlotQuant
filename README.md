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
    - **Intensity Profile View:** Real-time vertical profile plot to validate signal peaks and background levels.
    - **Loading Correlation and Biological Shift Plot:** A specialized visualization to distinguish between technical loading variability and true biological changes.
    - **ROI QC:** Real-time feedback on lane width consistency to prevent selection errors.
- **Rotation Alignment:** Interactive slider to rotate blots for perfect vertical alignment.
- **Advanced Background Subtraction:** Lane-specific median calculation to address gradient backgrounds.
- **Group Management:** Editable history dropdown for group names to streamline analysis of multiple blots.
- **Normalization:** Automatically normalize target proteins against loading controls (e.g., Actin, GAPDH).
- **Data Export:** Export comprehensive results to Excel or open data directly in GraphPad Prism.
- **Undo & Shortcuts:** Full undo support for ROI drawing with `Ctrl+Z` shortcut.
- **Data Import:** Reload previous datasets from Excel to reuse loading control data across multiple analyses.
- **Visual Feedback:** Real-time overlay of selected regions and lane dividers, with an integrated "How to" guide for new users.

## Methods

BlotQuant employs a robust image processing pipeline to quantify protein bands:

### 1. Preprocessing
The application converts the input image to grayscale for intensity analysis. To ensure accurate lane separation, users can apply **Rotation Alignment** (using BICUBIC interpolation). This step is crucial for aligning bands vertically, which simplifies the subsequent lane division and prevents signal overlap between adjacent samples.

### 2. ROI Selection
Users define a Region of Interest (ROI) that encompasses all bands of a specific protein across multiple lanes. This ROI can be dynamically resized and moved to perfectly frame the signal. For convenience, an **Undo** function (and `Ctrl+Z`) allows users to quickly clear the last drawn ROI.

### 3. Lane Separation
Based on the defined **Replicate Count**, the ROI is divided into equal lanes. For experiments with "Equal N" settings, the software can automatically handle paired Control and Treatment groups within a single ROI selection. Draggable separators allow for manual fine-tuning if lane spacing is irregular.

### 4. Quantification
Once the lanes are defined, individual band intensities are calculated:
- **Lane-Specific Background Subtraction:** Unlike global subtraction, BlotQuant calculates a unique **Background Intensity** for each lane using the **25th percentile** of pixels within its specific boundaries. This makes the quantification robust against tight ROI selections and addresses background gradients (e.g., darker on one side).
- **Integrated Density:** For each lane, the software calculates the sum of `(Pixel Intensity - Background)` for all pixels above a dynamic threshold (Background + 0.2 * Standard Deviation). This sensitivity adjustment ensures accurate capture of faint bands while excluding noise.
- **Scientific Validation:** The **Intensity Profile** tool allows researchers to visualize the mean pixel intensity across the ROI width. This "peak" view (with separator lines) ensures that background subtraction isn't clipping the protein signal.
- **Inversion:** Automatically handles blots where bands are darker than the background (e.g., Ponceau S or Coomassie staining) by inverting pixel values for quantification.

### 5. Normalization and Statistics
- **Normalization:** Target protein intensities are divided by their respective loading control intensities from the same lane. Previous analysis results can be **Imported from Excel** to reuse loading control data for different targets.
- **Statistics:** A dedicated **Statistics** dropdown allows users to choose between **Student's t-test**, **Welch's t-test** (unpaired), or **Two-way ANOVA** to determine statistical significance between experimental groups.

## Citation

Users are requested to cite **Hauffe et al. 2026 (In submission)** when using BlotQuant.

## License
This software is free for academic and non-commercial research use.
Commercial use requires a separate license agreement.
See the LICENSE file for details.

## Credits

**Author:** Dr. Robert Hauffe

## Build Instructions

To build the standalone executable from source, follow these steps:

### 1. Build Environment
- Install requirements: `pip install -r requirements.txt`
- Install PyInstaller: `pip install pyinstaller`

### 2. Run Build
Use the following command to create the single-file executable (ensure `BlotQuant_icon.ico` is in the project root):

```bash
pyinstaller --noconfirm --onefile --windowed --icon "BlotQuant_icon.ico" --add-data "BlotQuant_icon.ico;." --name "BlotQuant" --exclude-module "PyQt6" main.py
```

## Current Build Details (2026-02-17)
- **Version:** 1.2.0
- **SHA-256 Checksum:** `7977AF1360FBC04AD0088677344739BBB86E6C7A02BF6B0A2292377D3D0DEF9A`

To verify the integrity of your `BlotQuant.exe`, you can run the following command in PowerShell:
```powershell
Get-FileHash -Path "BlotQuant_v1.2.0.exe" -Algorithm SHA256
```
