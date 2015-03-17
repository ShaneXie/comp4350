//
//  foodListTableViewController.swift
//  CTS
//
//  Created by Shane on 2015-03-16.
//  Copyright (c) 2015 Comp4350Team7. All rights reserved.
//

import UIKit

class foodListTableViewController: UITableViewController {

    var tableData: Array<AnyObject> = []
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let inset:UIEdgeInsets = UIEdgeInsetsMake(20, 0, 0, 0)
        self.tableView.contentInset = inset

        request(.GET, "http://4350.intpointer.com/api/getAllFood/")
            .responseJSON {(request, response, reJson, error) in
                var foods = JSON(reJson!)
                var name = ""
                var cal = ""
                var type = ""
                var item = ""
                
                println(foods["foods"].count)
                println(foods["foods"][0]["fName"].stringValue)
                
                for idx in 0..<foods["foods"].count{
                    name = foods["foods"][idx]["fName"].stringValue
                    cal = foods["foods"][idx]["fCalorie"].stringValue
                    type = foods["foods"][idx]["fType"].stringValue
                    item = "\(name)\t\t\t\(cal)\t\t\(type)"
                    println(item)
                    self.tableData.append(item)
                }

                self.tableView.reloadData()
        }
        
        
        // Uncomment the following line to preserve selection between presentations
        //self.clearsSelectionOnViewWillAppear = false

        // Uncomment the following line to display an Edit button in the navigation bar for this view controller.
        //self.navigationItem.rightBarButtonItem = self.editButtonItem()
    }
    

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    // MARK: - Table view data source

    override func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        // #warning Potentially incomplete method implementation.
        // Return the number of sections.
        return 1
    }

    override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // #warning Incomplete method implementation.
        // Return the number of rows in the section.
        return tableData.count
    }

    
    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        
        let cellId:String = "foodcell"
        
        var cell:UITableViewCell = tableView.dequeueReusableCellWithIdentifier(cellId) as UITableViewCell


        cell.textLabel?.text = tableData[indexPath.row] as? String
        
        

        return cell
    }
    

    
    // Override to support conditional editing of the table view.
    override func tableView(tableView: UITableView, canEditRowAtIndexPath indexPath: NSIndexPath) -> Bool {
        // Return NO if you do not want the specified item to be editable.
        return true
    }
    

    
    // Override to support editing the table view.
    override func tableView(tableView: UITableView, commitEditingStyle editingStyle: UITableViewCellEditingStyle, forRowAtIndexPath indexPath: NSIndexPath) {
        if editingStyle == .Delete {
            // Delete the row from the data source
            tableData.removeAtIndex(indexPath.row)
            tableView.deleteRowsAtIndexPaths([indexPath], withRowAnimation: .Fade)
        } else if editingStyle == .Insert {
            // Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view
        }    
    }
    

    /*
    // Override to support rearranging the table view.
    override func tableView(tableView: UITableView, moveRowAtIndexPath fromIndexPath: NSIndexPath, toIndexPath: NSIndexPath) {

    }
    */

    /*
    // Override to support conditional rearranging of the table view.
    override func tableView(tableView: UITableView, canMoveRowAtIndexPath indexPath: NSIndexPath) -> Bool {
        // Return NO if you do not want the item to be re-orderable.
        return true
    }
    */

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        // Get the new view controller using [segue destinationViewController].
        // Pass the selected object to the new view controller.
    }
    */

}
