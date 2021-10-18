package com.finance.data.controller;

import com.finance.data.entity.Cryptocurrency;
import com.finance.data.service.CryptocurrencyService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.validation.Valid;

@RestController
@RequestMapping(value = "/api/cryptocurrency")
public class CryptocurrencyController {

    @Autowired
    private CryptocurrencyService cryptocurrencyService;

    @PostMapping(value = "", consumes = "application/json", produces = "application/json")
    public ResponseEntity<Cryptocurrency> saveApi (@Valid @RequestBody Cryptocurrency cryptocurrency) {
        return ResponseEntity.ok().body(cryptocurrencyService.saveCryptocurrency(cryptocurrency));
    }
}
