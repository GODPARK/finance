package com.finance.data.repository;

import com.finance.data.entity.KoreaStock;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface KoreaStockRepository extends JpaRepository<KoreaStock, Long> {
}
