# Predictive Code Compression

## 👤 Member 1 — [Input, Menu, Quantizer Calculations & Compression Core]
<!-- Ahmed Hassan -->
### Responsibilities

- [ ] Program Menu

Compression

Decompression

Exit


- [ ] Dynamic Inputs

Load image

Get number of quantization bits

Compute:

Step size / Range

Quantization values

De-quantization values




- [ ] Compression Function (excluding predictor)

Call predictor (done by Member 2)

Call quantizer

Generate:

Quantized image

Encoded bits

Compression ratio (shared with member 3)





- [ ] Outputs

Working menu system

Correct quantization logic

Partial compression code



---

## 👤 Member 2 — [2D Predictor + Error Calculation + Preparing All 6 Required Images]
<!-- Sami Anwer -->
### Responsibilities

- [ ] Implement the 2D predictor exactly as taught in lecture

e.g., (A+B)/2 or JPG-style predictor



- [ ] Compute

Predicted image

Error image (Original − Predicted)



- [ ] Pass Error Image → Quantization (member 1)


- [ ] Produce the following images

Original

Predicted

Error

(Quantized + Dequantized from others)




- [ ] Outputs

Predictor function

Predicted image

Error image

6 images pipeline partially completed



---

## 👤 Member 3 — [Decompression, Rebuilding Image & Final Outputs]
<!-- Ahmed Awwad -->
### Responsibilities

- [ ] Decompression Function

Read quantized data

De-quantize

Reconstruct error

Reconstruct final decompressed image using predictor



- [ ] Display All Required Images (6 total)

Original

Predicted

Error

Quantized

De-quantized

Final decompressed image



- [ ] Compute Compression Ratio

Work with Member 1



- [ ] (Bonus) If time allows: Apply on RGB image.



- [ ] Outputs

Dequantized image

Decompressed (final) image

Display window for 6 images

Compression ratio



---

## 📌 Final Summary Table

### Member Tasks

1. Menu + Input + Quantizer + Step size + Half of Compression
2. 2D Predictor + Predicted image + Error image + Prepare image pipeline
3. Decompression + Rebuild image + Display 6 images + Compression ratio

