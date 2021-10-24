package com.finance.data.controller;

import com.finance.data.entity.USStock;
import com.finance.data.service.USStockService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.validation.Valid;

@RestController
@RequestMapping(value = "/api/us_stock")
public class USStockController {

    @Autowired
    private USStockService usStockService;

    @PostMapping(value = "", consumes = "application/json", produces = "application/json")
    public ResponseEntity<USStock> saveApi(@Valid @RequestBody USStock usStock) {
        return ResponseEntity.ok().body(usStockService.saveUSStock(usStock));
    }
}
