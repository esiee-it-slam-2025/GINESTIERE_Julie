'use client';

import React from 'react';
import { QRCodeSVG } from 'qrcode.react';

interface QRCodeProps {
  value: string;
  size?: number;
  level?: 'L' | 'M' | 'Q' | 'H';
  includeMargin?: boolean;
  bgColor?: string;
  fgColor?: string;
  className?: string;
}

/**
 * A simple QR code generator component that outputs an SVG QR code
 * 
 * @param value - The content to encode in the QR code (text/URL)
 * @param size - Size of the QR code in pixels (default: 128)
 * @param level - Error correction level (default: 'M')
 * @param includeMargin - Whether to include a margin (default: true)
 * @param bgColor - Background color (default: '#FFFFFF')
 * @param fgColor - Foreground color (default: '#000000')
 * @param className - Optional CSS class name
 */
const QRCode: React.FC<QRCodeProps> = ({
  value,
  size = 128,
  level = 'M',
  includeMargin = true,
  bgColor = '#FFFFFF',
  fgColor = '#000000',
  className,
}) => {
  return (
    <QRCodeSVG
      value={value}
      size={size}
      level={level}
      includeMargin={includeMargin}
      bgColor={bgColor}
      fgColor={fgColor}
      className={className}
    />
  );
};

export default QRCode;