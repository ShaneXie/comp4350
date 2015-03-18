//
//  SecondViewController.swift
//  CTS
//
//  Created by Shane on 2015-03-14.
//  Copyright (c) 2015 Comp4350Team7. All rights reserved.
//

import UIKit

class BMIViewController: UIViewController {

    @IBOutlet weak var weightDisplay: UILabel!
    @IBOutlet weak var heightDisplay: UILabel!
    @IBOutlet weak var BMIDisplay: UILabel!
    @IBOutlet weak var weightSlider10: UISlider!
    @IBOutlet weak var weightSlider1: UISlider!
    @IBOutlet weak var heightSlider10: UISlider!
    @IBOutlet weak var heightSlider1: UISlider!
    
    @IBAction func sliderUpdate(sender: UISlider) {
        
        var weight = Float(lroundf(weightSlider1.value))/2.0
        weight = weight + Float(lroundf(weightSlider10.value)*10)
        var height = Float(lroundf(heightSlider1.value))/2.0
        height = height + Float(lroundf(heightSlider10.value)*10)
        //var height = Float(lroundf(heightSlider10.value)*10+lroundf(heightSlider1.value)/2)
        var BMI = Float(lroundf(weight/height/height*1000000))/100.0
        
        weightDisplay.text = "\(weight)"
        heightDisplay.text = "\(height)"
        BMIDisplay.text = "\(BMI)"
    }
    


}

