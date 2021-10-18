package com.finance.data.controller;

import com.finance.data.entity.KoreaStock;
import com.finance.data.service.KoreaStockService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.validation.Valid;

@RestController
@RequestMapping(value = "/api/korea_stock")
public class KoreaStockController {

    @Autowired
    private KoreaStockService koreaStockService;

    @PostMapping(value = "", consumes = "application/json", produces = "application/json")
    public ResponseEntity<KoreaStock> saveApi(@Valid @RequestBody KoreaStock koreaStock) {
        return ResponseEntity.ok().body(koreaStockService.saveKoreaStock(koreaStock));
    }
}
