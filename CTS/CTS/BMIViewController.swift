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
    
    @IBOutlet weak var weightDisplay2: UILabel!
    @IBOutlet weak var heightDisplay2: UILabel!
    @IBOutlet weak var weightDisplay2unit: UILabel!
    @IBOutlet weak var heightDisplay2unit: UILabel!
    
    @IBAction func sliderUpdate(sender: UISlider) {
        
        var weight = Float(lroundf(weightSlider1.value))/2.0
        weight = weight + Float(lroundf(weightSlider10.value)*10)
        var height = Float(lroundf(heightSlider1.value))/2.0
        height = height + Float(lroundf(heightSlider10.value)*10)
        var weight2 = Float(lroundf(weight/0.4536*10))/10.0
        var height2 = Float(lroundf(height/30.48*100))/100.0
        var BMI = Float(lroundf(weight/height/height*1000000))/100.0
        
        weightDisplay.text = "\(weight)"
        heightDisplay.text = "\(height)"
        weightDisplay2.text = "\(weight2)"
        heightDisplay2.text = "\(height2)"
        BMIDisplay.text = "\(BMI)"
    }
    
    @IBAction func toggle(sender: UISegmentedControl) {
        if sender.selectedSegmentIndex==0{
            weightDisplay2.hidden = true
            heightDisplay2.hidden = true
            weightDisplay2unit.hidden = true
            heightDisplay2unit.hidden = true
        }else{
            weightDisplay2.hidden = false
            heightDisplay2.hidden = false
            weightDisplay2unit.hidden = false
            heightDisplay2unit.hidden = false
        }
    }


}

